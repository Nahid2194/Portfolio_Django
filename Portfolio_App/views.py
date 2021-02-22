from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Portfolio_App.models import Skill, Project, Portfolio
from Portfolio_App.forms import LoginForm, SkillForm, ProjectForm, PortfolioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

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
                return HttpResponseRedirect(reverse('admin_form'))

    return render(request, 'adminLogin/login.html', context={'form': form, 'name': 'Login'})


@login_required
def admin_form(request):
    return render(request, 'adminLogin/nav_form.html',)


@login_required
def add_skills(request):
    form = SkillForm()

    return render(request, 'adminLogin/submit_form.html', context={'form': form, 'name': 'Add Skill'})


@login_required
def add_portfolio(request):
    form = PortfolioForm()
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_pic = form.save(commit=False)
            portfolio_pic.save()
            return HttpResponseRedirect(reverse('admin_form'))

    return render(request, 'adminLogin/submit_form.html', context={'form': form, 'name': 'Add Portfolio'})


@login_required
def add_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return HttpResponseRedirect(reverse('admin_form'))

    return render(request, 'adminLogin/submit_form.html', context={'form': form, 'name': 'Add Project Details'})
    # template_name = 'adminLogin/submit_form.html'
    # fields = ['title', 'project_url', 'project_pic']

    # def form_valid(self, form):
    #     form.save()
    #     return HttpResponseRedirect(reverse('admin_form'))
