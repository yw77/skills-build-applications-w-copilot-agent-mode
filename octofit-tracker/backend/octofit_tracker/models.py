# models.py for OctoFit Tracker
# Define models for users, teams, activities, leaderboard, and workouts

from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_superhero = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()
    def __str__(self):
        return f"{self.user.email} - {self.activity_type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team.name} - {self.points}"
