import csv

from django.db import migrations

from ..models import Standing


def load_initial_data(app, schema_editor):
    with open('PremierLeagueStanding/premier-league-tables.csv', 'r', encoding='utf-8') as input_file:
        input_file.readline()
        reader = csv.reader(input_file, delimiter=',')

        for row in reader:
            standing = Standing(Season_End_Year=int(row[0]), Team=(row[1]), Rk=int(row[2]), MP=int(row[3]),
                                W=int(row[4]), D=int(row[5]), L=int(row[6]), GF=int(row[7]), GA=int(row[8]),
                                GD=int(row[9]),
                                Pts=int(row[10]), Notes=row[11])
            standing.save()


class Migration(migrations.Migration):
    dependencies = [
        ('PremierLeagueStanding', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
