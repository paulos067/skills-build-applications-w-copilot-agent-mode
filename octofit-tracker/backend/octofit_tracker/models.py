from django.db import models

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	duration = models.IntegerField()
	team = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
	user = models.CharField(max_length=100)
	team = models.CharField(max_length=100)
	score = models.IntegerField()
	def __str__(self):
		return f"{self.user} - {self.team}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	difficulty = models.CharField(max_length=50)
	def __str__(self):
		return self.name
