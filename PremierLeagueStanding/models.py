import csv
from django.db import models


# Create your models here.

class Standing(models.Model):
    Season_End_Year = models.IntegerField()
    Team = models.CharField(max_length=100)
    Rk = models.IntegerField()
    MP = models.IntegerField()
    W = models.IntegerField()
    D = models.IntegerField()
    L = models.IntegerField()
    GF = models.IntegerField()
    GA = models.IntegerField()
    GD = models.IntegerField()
    Pts = models.IntegerField()
    Notes = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.Season_End_Year} - {self.Team} - Rank: {self.Rk}"
    @staticmethod
    def get_all():
        standings = []

        with open('PremierLeagueStanding/premier-league-tables.csv', 'r', encoding='utf-8') as input_file:
            input_file.readline()
            reader = csv.reader(input_file, delimiter=',')

            for row in reader:
                standings.append(Standing(Season_End_Year=int(row[0]), Team=row[1], Rk=int(row[2]), MP=int(row[3]),
                                          W=int(row[4]), D=int(row[5]), L=int(row[6]), GF=int(row[7]),
                                          GA=int(row[8]), GD=int(row[9]), Pts=int(row[10]), Notes=row[11]))

        return standings

    @staticmethod
    def get_team_in_season(Season_End_Year, Team):
        all_standings = Standing.get_all()
        try:
            for standing in all_standings:
                if standing.Season_End_Year == Season_End_Year:
                    if standing.Team == Team:
                        return Season_End_Year, Team
        except Standing.DoesNotExist:
            return None
