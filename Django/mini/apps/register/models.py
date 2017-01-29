from __future__ import unicode_literals
import re
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

def containnumber(string):
    return bool(re.search(r'\d', string))

def email_validation(value):
    email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if not email_re.match(value):
        raise ValidationError(_('{} is not a valid email'.format(value)))
        print 'not a valid email'

def valid_name(value):
    if containnumber(value):
        raise ValidationError(_('Invalid value'))
        print 'bad name'
    if len(value)<3:
        raise ValidationError(_('Invalid value'))
        print 'bad name'
    if len(value)>100:
        raise ValidationError(_('Invalid value'))
        print 'bad name'
def valid_password(value):
    if len(value)<9:
        raise ValidationError(_('Bad password'))
        print 'bad password'

class Users(models.Model):
    first_name = models.CharField(max_length=100,validators = [valid_name])
    last_name = models.CharField(max_length=100,validators = [valid_name])
    email = models.EmailField(validators = [email_validation])
    password = models.CharField(max_length=100,validators = [valid_password])
