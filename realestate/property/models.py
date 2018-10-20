# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django_countries.fields import CountryField
from profiles.models import Profile

# Create your models here.

class PropertyManager(models.Manager):
    def get_all_available_units_for_rent(self):
        units_for_rent = self.filter(property_type='UN', is_rental=True, is_available=True, is_published=True)
        return units_for_rent
    def get_all_available_townhouses_for_rent(self):
        townhouses_for_rent = self.filter(property_type='TW', is_rental=True, is_available=True, is_published=True)
        return townhouses_for_rent
    def get_all_available_houses_for_rent(self):
        houses_for_rent = self.filter(property_type='HS', is_rental=True, is_available=True, is_published=True)
        return houses_for_rent
    def get_all_available_villas_for_rent(self):
        villas_for_rent = self.filter(property_type='VL', is_rental=True, is_available=True, is_published=True)
        return villas_for_rent

class Property(models.Model):
    PROPERTY_CHOICES = (
        ('UN', 'Unit'),
        ('TW', 'TownHouse'),
        ('VL', 'Villa'),
        ('HS', 'House'),
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    is_available = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    is_rental = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    available_date = models.DateField(null=True, blank=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=3000, blank=True, null=True)

    address1 =  models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)

    property_type = models.CharField(
      max_length = 2,
      choices = PROPERTY_CHOICES,
      default = 'UN',
    )
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    carparking = models.IntegerField(blank=True, null=True)
    built_up_area = models.CharField(max_length=50, blank=True, null=True)

    profile = models.ForeignKey(Profile, blank=True, null=True, related_name='properties', on_delete=models.CASCADE)

    objects = PropertyManager()

    def get_all_images(self):
        images = self.images.all()
        return images

    def __str__(self):
        return "%s - %s %s"%(self.name, self.profile.first_name, self.profile.last_name)


class Image(models.Model):
    property = models.ForeignKey(Property, related_name='images')
    file = models.ImageField(upload_to='static/images/')
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s'%(self.property.name, self.file)
