from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from .models import Skill, Project, Portfolio


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': "Username"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
