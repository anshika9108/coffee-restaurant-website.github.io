from django.shortcuts import render
from coffee.models import Student
from coffee.models import Image


from django import forms
from coffee.models import WangUser


class EmpForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = "__all__"



class UserReg(forms.ModelForm):
    class Meta:
        model = WangUser
        fields = "__all__"

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'




