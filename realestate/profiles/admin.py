# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from profiles.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'mobile', 'country', 'state', 'city', 'address1', 'address2')
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


admin.site.register(Profile, ProfileAdmin)
