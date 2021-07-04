from django import forms
from django.forms import widgets
from rolodex_app.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = "__all__"
        fields = (
            'name',
            'gender',
            'race',
            'birthday',
            'street',
            'city',
            'email',
            'phone_number',
            'mobile_number'
            )

