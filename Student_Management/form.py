from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student_db
class Admin(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class Student_form(forms.Form):
    Name=forms.CharField(max_length=50)
    Contact=forms.IntegerField()
    Mail=forms.EmailField()
    
class Student_db(forms.ModelForm):
    class Meta:
        model=Student_db
        fields=['Name','Contact','Mail']
