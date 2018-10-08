import sys
import os



from django.conf import settings
from django.template.defaultfilters import slugify

from django import forms
from .models import Property, PropertyType, Location, Image


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'is_available', 'is_sale', 'is_rental', 
                  'available_date', 'price', 'kicker', 'description', 'property_type'] 

