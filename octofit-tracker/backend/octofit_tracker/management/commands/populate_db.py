from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Workouts
        iron_workout = Workout.objects.create(name='Iron Training', description='Strength and armor')
        shield_workout = Workout.objects.create(name='Shield Training', description='Defense and tactics')
        bat_workout = Workout.objects.create(name='Bat Training', description='Stealth and gadgets')
        super_workout = Workout.objects.create(name='Super Training', description='Flight and strength')

        # Create Activities
        Activity.objects.create(user=tony, workout=iron_workout, duration=60)
        Activity.objects.create(user=steve, workout=shield_workout, duration=45)
        Activity.objects.create(user=bruce, workout=bat_workout, duration=50)
        Activity.objects.create(user=clark, workout=super_workout, duration=70)

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
