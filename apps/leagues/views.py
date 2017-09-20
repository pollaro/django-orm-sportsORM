from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		# #Baseball only:
		# "leagues":League.objects.filter(sport='Baseball')
		# #Womens only leagues:
		# 'leagues':League.objects.filter(name__contains='Womens')
		# #Hockey leagues:
		# 'leagues':League.objects.filter(name__contains='Hockey')|League.objects.filter(sport__contains='Hockey')
		# #Non football sports:
		# 'leagues':League.objects.exclude(sport='Football')
		# #Leagues that are "conferences":
		# 'leagues':League.objects.filter(name__contains='Conference')
		# #Leagues in the atlantic region
		# 'leagues':League.objects.filter(name__contains='Atlantic')
		# #Teams Based in Dallas
		# 'teams':Team.objects.filter(location__contains='Dallas')
		# #Teams Named Raptors
		# 'teams':Team.objects.filter(team_name__contains='Raptors')
		# #Teams in Cities that have City in them
		# 'teams':Team.objects.filter(location__contains='City')
		# #Teams that begin with T
		# 'teams':Team.objects.filter(team_name__startswith='T')
		# #All teams ordered by location
		# 'teams':Team.objects.order_by('location')
		# #All teams ordered by reverse team name
		# 'teams':Team.objects.order_by('-team_name')
		# #Players with last name Cooper
		# "players": Player.objects.filter(last_name='Cooper')
		# #Players with first name Joshua
		# "players": Player.objects.filter(first_name='Joshua')
		# #Players with last name cooper except ones with Joshua
		# "players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')
		# #Players with first name Alexander or Wyatt
		# "players": Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt')

		#All teams in the Atlanic Soccer Conference
		"teams": Team.objects.filter(location='Atlantic',league__sport='Soccer',league__name__contains='Conference')
		#All players on Boston Penguins
		"players": Player.objects.filter(curr_team__team_name='Penguins',curr_team__location='Boston')
		#All players in International Collegiate Baseball Conference
		"players":Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference')
		#All players in American Conference of Amatuer Football with last name Lopez
		"players":Player.objects.filter(curr_team__league__name='American Conference of Amateur Football',last_name='Lopez')
		#All football players
		"players":Player.objects.filter(all_teams__league__sport='Football')
		#Teams with current player named Sophia
		"teams": Team.objects.filter(curr_players__first_name='Sophia')
		#Leauges with current player named Sophia
		"leagues": League.objects.filter(teams__curr_players__first_name='Sophia')
		#Everyone with last name Flores not currently on Washington Roughriders
		"players": Player.objects.filter(last_name='Flores').exclude(curr_team__location='Washington',curr_team__team_name='Roughriders')
		#All teams Samuel Evans played with
		'teams': Team.objects.filter(all_players__first_name='Samuel',all_players__last_name='Evans')
		#All players with Manitoba Tiger-Cats
		'players':Player.objects.filter(all_teams__team_name='Tiger-Cats',all_teams__location='Manitoba')
		#All players formerly with Wichita Vikings
		'players':Player.objects.filter(all_teams__team_name='Vikings',all_teams__location='Wichita').exclude(curr_team__team_name='Vikings',curr_team__location='Wichita')
		#Every team Jacob Gray played for before Oregon Colts
		'teams':Team.objects.filter(all_players__first_name='Jacob',all_players__last_name='Gray').exclude(location='Oregon',team_name='Colts')
		#Everyone name Joshua who has played in Atlantic Federation of Amateur Baseball Players
		'players':Player.objects.filter(all_teams__league__name='Atlantic Federation of Amateur Baseball Players')
		#All teams that have had 12 or more players
		'teams':Team.objects.annotate(plyrs=Count('all_players')).filter(plyrs__gt=12)
		#All players and count of teams for, sorted by number of teams
		'players':Player.objects.annotate(tms=Count('all_teams')).all().order_by('tms')

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
