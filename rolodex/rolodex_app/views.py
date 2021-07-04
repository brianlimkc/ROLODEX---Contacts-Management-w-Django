from django.shortcuts import render, redirect
from rolodex_app.models import Contact
from rolodex_app.forms import ContactForm
import requests
from bs4 import BeautifulSoup
from django.contrib import messages

# Create your views here.

def index(request):

    if request.method == "POST":

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            race = form.cleaned_data['race']
            birthday = form.cleaned_data['birthday']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            mobile_number = form.cleaned_data['phone_number']

            contact = Contact(
                name=name,
                gender=gender,
                race=race,
                birthday=birthday,
                street=street,
                city=city,
                email=email,
                phone_number=phone_number,
                mobile_number=mobile_number
            )

            contact.save()

            messages.success(request, "Contact saved!")

            return redirect("index_page")

    contacts = Contact.objects.all()

    form = ContactForm()

    return render(
        request,
        "rolodex_app/index.html",
        {"contact_list": contacts,
         "form": form})


def search(request):

    query = request.GET.get("q")

    search_result = Contact.objects.filter(name__icontains=query)

    form = ContactForm()

    return render(
        request,
        "rolodex_app/index.html",
        {"contact_list": search_result,
         "form": form})


def show(request, id):

    try:
        contact = Contact.objects.get(pk=int(id))
    except Contact.DoesNotExist:
        messages.error(request,
        "Incorrect request, please try again")
        return redirect("index_page")

    form = None
    
    # if request.GET.get("edit") == "true":
    #     form = ContactForm(instance=contact)

    if request.method == "POST":
        if request.GET.get("edit") == "true" :
            form = ContactForm(request.POST, instance=contact)

            if form.is_valid():
                form.save()
                messages.success(request, "Contact edited!")
                return redirect("index_page")
        else:
            form = ContactForm(instance=contact)
    

    if request.GET.get("delete") == "true" and request.method == "POST":
        contact.delete()
        messages.success(request, "Contact deleted!")
        return redirect("index_page")

    return render(
        request,
        "rolodex_app/show.html",
        {"contact": contact,
         "form": form}
    )


def add_random(request):

    if request.method == "POST":

        URL = "https://www.fakepersongenerator.com/?new=fresh"

        page = requests.get(URL)

        parsed_html = BeautifulSoup(page.content, "html.parser")

        new_person_list = parsed_html.find_all(
            "body")

        for item in new_person_list:

            name = item.find("p", class_="name").text
            gender = item.find(lambda tag: tag.name ==
                               "p" and "Gender: " in tag.text).find("b").text
            race = item.find(lambda tag: tag.name ==
                             "p" and "Race: " in tag.text).find("b").text
            birthday = item.find(lambda tag: tag.name ==
                                 "p" and "Birthday: " in tag.text).find("b").text
            street = item.find(lambda tag: tag.name ==
                               "p" and "Street: " in tag.text).find("b").text
            city = item.find(
                lambda tag: tag.name == "p" and "City, State, Zip: " in tag.text).find("b").text
            phone = item.find(lambda tag: tag.name ==
                              "p" and "Telephone: " in tag.text).find("b").text
            mobile = item.find(lambda tag: tag.name ==
                               "p" and "Mobile: " in tag.text).find("b").text
            email = item.find(
                'div', class_='info-detail').find("input").get("value")

            contact = Contact(
                name=name,
                gender=gender,
                race=race,
                birthday=birthday,
                street=street,
                city=city,
                email=email,
                phone_number=phone,
                mobile_number=mobile
            )

            contact.save()

    contacts = Contact.objects.all()

    form = ContactForm()

    return render(
        request,
        "rolodex_app/index.html",
        {"contact_list": contacts,
         "form": form})
