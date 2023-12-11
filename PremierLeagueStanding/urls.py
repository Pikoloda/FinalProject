from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_standings, name='all_standings' ),
    path('PremierLeaque/<Season_End_Year>/<Team>', views.team_details_in_season, name='find_by_team_and_season'),
]