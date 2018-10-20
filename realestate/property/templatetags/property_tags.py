import os
import sys

from django.conf import settings
from django import template
from property.models import Property


register = template.Library()
