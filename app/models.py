from django.db import models
from django.core import validators
from django import forms

# Create your models here.
def check_for_a(name):
    if name[0]=='a':
        raise forms.ValidationError('error startswith a')
class PersonForm(models.Model):
    name=models.CharField(max_length=100,validators=[check_for_a,validators.MinLengthValidator])
    age=models.IntegerField()
    email=models.EmailField(validators=[validators.EmailValidator('email is not valid')])
    url=models.URLField()
    phone=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    gender=models.CharField(max_length=10,choices=[('MALE','male'),('FEMALE','female')],)

