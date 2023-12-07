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

    @staticmethod
    def get_all():
        standings = []

        with open('PremierLeagueStanding/premier-league-tables.csv', 'r', encoding='utf-8') as input_file:
            input_file.readline()
            reader = csv.reader(input_file, delimiter=',')

            for row in reader:
                standings.append(Standing(*row))

        return standings
