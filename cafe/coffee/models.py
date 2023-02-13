from django.db import models
from django import forms
from django.forms import ModelForm

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=30)
    contact=models.IntegerField
    password=models.CharField(max_length=20)
    class Meta:
        db_table = "student"



class Image(models.Model):
    photo=models.ImageField(upload_to="myimage") #we ll store here
    data=models.DateTimeField(auto_now_add=True)
# Create your models here.
class WangUser(models.Model):
    username = models.CharField(max_length=32, unique = True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
