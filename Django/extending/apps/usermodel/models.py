from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.db import models

class age(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DateTimeField(auto_now = False, auto_now_add=False)
