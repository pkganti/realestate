# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render
from django.template import loader
from django.template.loader import select_template, get_template

from .models import Property, Location, PropertyType

# Create your views here.


def home(request):

    c = {}
    return render(request, 'home.html', c)
    


def property_login(request):
    c = {}
    return render(request, 'login.html', c)



def user_registration(request):
    c = {}
    return render(request, 'user_register.html', c)



def property_registration(request):
    c = {}
    return render(request, 'property_register.html', c)




