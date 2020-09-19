from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    password1= forms.CharField(widget=forms.PasswordInput())
    password2= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1','password2']
        
        
class CreateQuestion(ModelForm):
    class Meta:
        model = create_question
        fields = '__all__'
        
     
class CreateAnswer(ModelForm):
    class Meta:
        model = create_answer
        fields = ['answer']
        