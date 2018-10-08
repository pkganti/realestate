# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django_countries.fields import CountryField

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    address1 =  models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField()
    postcode = models.CharField(max_length=10, blank=True, null=True) 


class PropertyType(models.Model):
    PROPERTY_CHOICES = (
        ('UN', 'Unit'),
        ('TW', 'TownHouse'),
        ('VL', 'Villa'),
        ('HS', 'House'),
    )
    prop_type = models.CharField(
      max_length = 2,
      choices = PROPERTY_CHOICES,
      default = 'UN',
    )
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    carparking = models.IntegerField()
    built_up_area = models.CharField(max_length=50, blank=True, null=True)


class Property(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    location = models.ForeignKey('Location', related_name = 'properties')
    is_available = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    is_rental = models.BooleanField(default=False)
    available_date = models.DateTimeField()
    price = models.CharField(max_length=50, blank=True, null=True)
    kicker = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    property_type = models.ForeignKey('PropertyType', related_name = 'properties')


class Image(models.Model):
    property = models.ForeignKey(Property, related_name='images')
    file = models.ImageField(upload_to='images')
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s'%(self.property, self.file)


    
    
    
