from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from . import models
from .models import Standing


def all_standings(request):
    standings = models.Standing.get_all()
    return render(request, 'PremierLeagueStanding/all_standings.html', {
        'standings': standings
    })


def team_details_in_season(request, Season_End_Year, Team):
    found_team = models.Standing.get_team_in_season(Season_End_Year, Team)
    return render(request, 'PremierLeagueStanding/team_details.html', {
        'team': found_team
    })
# def team_details_in_season(request, Season_End_Year, Team):
#     found_team = Standing.objects.filter(Season_End_Year=Season_End_Year, Team=Team)
#
#     context = {
#         'found_team': found_team,
#         'Season': Season_End_Year,
#         'Team': Team,
#     }
