from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите логин '}))
    name = forms.CharField(label = 'Имя и Фамилия', widget = forms.TextInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите имя и фамилию '}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите пароль еще раз '}))

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle u-none', 'placeholder': 'Введите пароль'}))
    

class TestForm(forms.Form): 
    CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"),) 

    q1 = forms.ChoiceField(choices= CHOICES,  widget = forms.CheckboxSelectMultiple())
    

