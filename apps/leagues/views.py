from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		#Baseball only:
		"leagues":League.objects.filter(sport='Baseball')
		#Womens only leagues:
		'leagues':League.objects.filter(name__contains='Womens')
		#Hockey leagues:
		'leagues':League.objects.filter(name__contains='Hockey')|League.objects.filter(sport__contains='Hockey')
		#Non football sports:
		'leagues':League.objects.exclude(sport='Football')
		#Leagues that are "conferences":
		'leagues':League.objects.filter(name__contains='Conference')
		#Leagues in the atlantic region
		'leagues':League.objects.filter(name__contains='Atlantic')
		#Teams Based in Dallas
		'teams':Team.objects.filter(location__contains='Dallas')
		#Teams Named Raptors
		'teams':Team.objects.filter(team_name__contains='Raptors')
		#Teams in Cities that have City in them
		'teams':Team.objects.filter(location__contains='City')
		#Teams that begin with T
		'teams':Team.objects.filter(team_name__startswith='T')
		#All teams ordered by location
		'teams':Team.objects.order_by('location')
		#All teams ordered by reverse team name
		'teams':Team.objects.order_by('-team_name')
		#Players with last name Cooper
		"players": Player.objects.filter(last_name='Cooper')
		#Players with first name Joshua
		"players": Player.objects.filter(first_name='Joshua')
		#Players with last name cooper except ones with Joshua
		"players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')
		#Players with first name Alexander or Wyatt
		"players": Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt')

		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
