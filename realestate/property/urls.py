from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from .views import *

urlpatterns = [
    url(r'^$', property_home, name="property_home"),
    url(r'^login/$', property_login, name="property_login"),
    url(r'^logout/$', property_logout, name="property_logout"),

    # Property Specific URLS
    url(r'^(?P<property_id>\d+)/$', property_view, name='property_view'),
    url(r'^registration/$', property_registration, name="property_registration"),
    url(r'^edit/(?P<property_id>\d+)/$', property_edit, name="property_edit"),
    url(r'^activate/(?P<property_id>\d+)/$', property_activate, name="property_activate"),

    # User specific URLS
    url(r'^user/registration/$', user_registration, name="user_registration"),
    url(r'^user/home/$', user_home, name="user_home"),
    url(r'^user/edit/(?P<profile_id>\d+)/$', user_edit, name="user_edit"),
]
