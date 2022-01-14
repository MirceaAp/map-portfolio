from django.shortcuts import render
from .models import Project


def home_page_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portofolio/homepage.html', context)


def test_page_view(request):
    return render(request, 'portofolio/testing.html', {})
