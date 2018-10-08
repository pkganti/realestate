from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', home, name="property_home"),
    url(r'^property/login/$', property_login, name="property_login"),
    url(r'^user/registration/$', user_registration, name="user_registration"),
    url(r'^property/registration/$', property_registration, name="property_registration"),

]

