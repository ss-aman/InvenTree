# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import User
admin.site.register(Permission)
admin.site.register(User)
