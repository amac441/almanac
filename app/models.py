from django.db import models
from django.forms import ModelForm
from django.contrib import admin

# Create your models here.

POSITION_CHOICES = (
    ('ColCoun', 'College Counselor'),
    ('CarCoach', 'Career Coach'),
    ('Prof', 'Professional'),
    ('Student', 'Student'),
    ('Other', 'Other'),
    )

class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    age = models.CharField(max_length=10, null=True)
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    problem = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.name

class SignupForm(ModelForm):
    class Meta:
        model=Signup

# admin.site.register(Signup)