from django.shortcuts import render, redirect
from Portfolio_App.models import Skill, Project, Portfolio
# Create your views here.


def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    portfolio_pics = Portfolio.objects.all()
    return render(request, 'Portfolio_App/index.html', context={'skills': skills, 'projects': projects, 'portfolio_pics': portfolio_pics})
