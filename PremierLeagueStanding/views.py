
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models



def all_standings(request):
    standings = models.Standing.get_all()
    return render(request, 'PremierLeagueStanding/all_standings.html', {
        'standings' : standings
    })
