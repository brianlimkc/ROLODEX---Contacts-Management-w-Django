# Generated by Django 3.2.5 on 2021-07-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile_number',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='contact',
            name='race',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='street',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='zipcode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]
