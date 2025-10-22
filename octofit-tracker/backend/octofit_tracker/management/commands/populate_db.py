from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from django.db import connection

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='pass', first_name='Steve', last_name='Rogers'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', first_name='Diana', last_name='Prince'),
        ]

        # Activities
        Activity.objects.create(user='ironman', type='Run', duration=30, team='Marvel')
        Activity.objects.create(user='captainamerica', type='Swim', duration=45, team='Marvel')
        Activity.objects.create(user='batman', type='Cycle', duration=60, team='DC')
        Activity.objects.create(user='wonderwoman', type='Yoga', duration=50, team='DC')

        # Leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='captainamerica', team='Marvel', score=90)
        Leaderboard.objects.create(user='batman', team='DC', score=95)
        Leaderboard.objects.create(user='wonderwoman', team='DC', score=98)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', difficulty='Hard')
        Workout.objects.create(name='Agility Training', description='Agility and speed drills', difficulty='Medium')
        Workout.objects.create(name='Endurance Run', description='Long distance running', difficulty='Hard')
        Workout.objects.create(name='Flexibility Flow', description='Yoga and stretching', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

        self.stdout.write(self.style.WARNING('Please create a unique index on the email field for users manually using mongosh:'))
        self.stdout.write(self.style.WARNING('db.users.createIndex({ "email": 1 }, { unique: true })'))
