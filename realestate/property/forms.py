import sys
import os

from datetime import datetime
from django.conf import settings
from django.template.defaultfilters import slugify

from django import forms
from django.forms.widgets import Widget, DateInput
from django.forms import ModelForm
from django.forms.formsets import BaseFormSet
from .models import Property, Image
from django_countries.fields import CountryField


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = [
                'name', 'is_published', 'is_available', 'available_date', 'is_sale', 'is_rental', 'price', 'summary', 'description', 'property_type', 'bedrooms', 'bathrooms', 'carparking', 'built_up_area', 'address1', 'address2', 'address3', 'city', 'state', 'country', 'postcode'
        ]
        widgets = {
            'is_published': forms.HiddenInput(),
            'available_date': forms.DateInput()
        }

class PropertyAdminForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = [
                'name', 'is_published', 'is_available', 'available_date', 'is_sale', 'is_rental', 'price', 'summary', 'description', 'property_type', 'bedrooms', 'bathrooms', 'carparking', 'built_up_area', 'address1', 'address2', 'address3', 'city', 'state', 'country', 'postcode'
        ]


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('file', )
