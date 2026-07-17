from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    context = {'name': 'Sash'}
    return render(
        request=request,
        template_name='home.html',
        context=context
    )

def about_me(request: HttpRequest) -> HttpResponse:
    skills = [
        'Python',
        'Chinese',
        'Chemistry',
        'Biology'
    ]
    return render(
        request=request,
        template_name='aboutme.html',
        context={'skills': skills}
    )
