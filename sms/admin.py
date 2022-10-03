# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Message, SiteConfiguration

admin.site.register(Message)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
