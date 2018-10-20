# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.conf import settings

from .forms import PropertyAdminForm
from .models import Property, Image

# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image
    extra = 3


class PropertyAdmin(admin.ModelAdmin):

    form = PropertyAdminForm
    inlines = [ImageInline]

    def save_model(self, request, obj, form, change):
        super(PropertyAdmin, self).save_model(request, obj, form, change)

        for afile in request.FILES.getlist('photos_multiple'):
            obj.images.create(file=afile)


admin.site.register(Property, PropertyAdmin)
