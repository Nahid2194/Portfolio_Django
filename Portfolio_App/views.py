from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Portfolio_App.models import Skill, Project, Portfolio
from Portfolio_App.forms import LoginForm
from django.urls import reverse
# Create your views here.


def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    portfolio_pics = Portfolio.objects.all()
    return render(request, 'Portfolio_App/index.html', context={'skills': skills, 'projects': projects, 'portfolio_pics': portfolio_pics})


def admin_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'Portfolio_App/login.html', context={'form': form})


def admin_form(request):
    return render(request, 'Portfolio_App/login.html',)
