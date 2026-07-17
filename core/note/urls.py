from django.urls import path
from . import views

urlpatterns = [
    path(
        route='',
        view=views.home,
        name='Home'
    ),
    path(
        route='aboutme/',
        view=views.about_me,
        name='About Me'
    ),
]
