from __future__ import unicode_literals

from django.db import models

class courses(models.Model):
    course = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
