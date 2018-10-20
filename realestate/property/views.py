# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pdb

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.loader import select_template, get_template
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory

from .models import Property, Image
from profiles.models import Profile
from .forms import PropertyForm, ImageForm
from profiles.forms import SignUpForm

# Create your views here.

def property_home(request):
    if request.POST:
        property_type = request.POST.get('property_type', None)
        loc_type = request.POST.get('loc_type', None)
        location = request.POST.get('location', None)
        starting_price = request.POST.get('starting_budget', None)
        ending_price = request.POST.get('ending_budget', None)

        # properties = Property.objects.filter(is_available=True, is_published=True).filter(property_type=property_type).filter(loc_type=location).filter(price__gte=int(starting_price), price__lte=int(ending_price))

        properties = Property.objects.filter(is_available=True, is_published=True).filter(city__iexact=location).filter(price__gte=int(starting_price), price__lte=int(ending_price))
        print properties

        c = {'properties': properties}
        return render(request, 'home.html', c)

    properties = Property.objects.filter(is_available=True, is_published=True);
    c = {'properties': properties}
    return render(request, 'home.html', c)

def user_home(request):
    if not request.user.is_authenticated():
        return redirect('property_home')
    user = request.user
    properties = Property.objects.filter(profile__user = user);
    c = {"properties": properties}
    return render(request, 'user_home.html', c)

def user_registration(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user_home')
    c = {}
    return render(request, 'user_register.html', c)

def user_edit(request, profile_id):
    if not request.user.is_authenticated():
        return redirect('property_login')
    if request.POST:
        pdb.set_trace()
    c = {}
    return render(request, 'user_edit.html', c)


def property_login(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user_home')
        else:
            message = "Invalid credentials. Please check your username or password"
            c = { "message": message }
            return render(request, 'login.html', c)
    c = {}
    return render(request, 'login.html', c)


def property_logout(request):
    logout(request)
    return redirect('property_home')

def property_registration(request):

    if not request.user.is_authenticated():
        # Redirecting the user to login page if not already logged in
        return redirect('property_login')

    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=5, max_num=5)
    if request.POST:
        propertyForm = PropertyForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if propertyForm.is_valid() and formset.is_valid():
            propertyForm = propertyForm.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            propertyForm.profile = profile
            propertyForm.save()
            position = 0
            for form in formset.cleaned_data:
                if not form.has_key('file'):
                    continue
                image = form['file']
                photo = Image(file= image, property = propertyForm, position = position)
                photo.save()
                position += 1
                # messages.success(request, "Your property has been successfully saved !!")
            return redirect('user_home')
        else:
            print propertyForm.errors, formset.errors
    else:
        propertyForm = PropertyForm()
        formset = ImageFormSet(queryset=Image.objects.none())

    return render(request, 'property_register.html', {'propertyForm': propertyForm, 'formset': formset })

def property_view(request, property_id):
    c = {}
    return render(request, 'property_register.html', c)

def property_edit(request, property_id):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=5, max_num=5)
    if not request.user.is_authenticated():
        # Redirecting the user to login page if not already logged in
        return redirect('property_view')

    if request.POST:
        property = Property.objects.get(pk=property_id)
        propertyForm = PropertyForm(request.POST, instance=property)
        formset = ImageFormSet(request.POST, request.FILES)
        if propertyForm.is_valid() and formset.is_valid():
            propertyForm.save()
            position = 0
            images = Image.objects.filter(property=property)
            for index, form in enumerate(formset):
                if form.cleaned_data:
                    if form.cleaned_data['id'] is None:
                        image = form.cleaned_data.get('file')
                        photo = Image(property = property, file= image, position = position)
                        photo.save()
                        # messages.success(request, "Your property has been successfully saved !!")
                    # elif form.cleaned_data['file'] is False:
                    #     photo = Image.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                    #     photo.delete()

                    else:
                        image = form.cleaned_data.get('file')
                        photo = Image(property = property, file= image, position = position)
                        d = Image.objects.get(id=images[index].id)
                        d.file = photo.file
                        d.save()
                    position += 1

            return redirect('user_home')
        else:
            print propertyForm.errors, formset.errors

    property = Property.objects.get(pk=property_id)
    propertyForm = PropertyForm(instance=property)
    formset = ImageFormSet(queryset=Image.objects.filter(property=property))

    return render(request, 'property_edit.html', {'property': property, 'propertyForm': propertyForm, 'formset': formset })

def property_activate(request, property_id):
    property = Property.objects.get(pk=property_id)
    if property.is_published:
        property.is_published = False
        property.save()
        return redirect('user_home')
    property.is_published = True
    property.save()
    return redirect('user_home')
