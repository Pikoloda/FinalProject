from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_standings, name='all_standings' ),
]