#!/usr/bin/python

import sys

# AB, H, 2B, 3B, HR, SB, CS, BB, IP, IPouts, HR, BB, SO
point_multipliers = [-.2,.6,.3,.5,.8,.2,-.4,.3,0,.14/3,-.62,-.14,.14]

f = open('data/stattracker_data.html', 'r')
input = f.readlines()


# put the player names in a map
player_name = dict()
for player_line in open('data/players.txt', 'r').readlines():
	if (player_line.startswith("m|")):
#		print player_line
		player_data = player_line.split("|")
		pname = "\"%s %s\"" % (player_data[3], player_data[4])
		pnum = player_data[1]
		player_name[pnum] = pname

#print player_name

# extract my roster from the "teams" section
my_roster = filter(lambda str: str.startswith("teams^"), input)[0].split("|")[2].split(",")

# put the player stats into a map
player_stats_raw = filter(lambda str: str.startswith("playerTotals^"), input)[0].split("^")[1].split("|")[1:]
my_team_logs = zip (player_stats_raw[::2], player_stats_raw[1::2])
# filter batters by AB, pitchers by IPouts.  Not perfect, but will work often enough
my_batter_logs = filter(lambda p : int(p[1].split(",")[0]) > 0, my_team_logs)
my_pitcher_logs = filter(lambda p : int(p[1].split(",")[9]) > 0, my_team_logs)


def dot_product(a, b):
	return sum(x*y for (x,y) in zip(a,b))
	

def points (player_log) :
	return dot_product(point_multipliers, map(float, player_log.split(",")))

for p in my_team_logs:
	try:
		pname = player_name[p[0]]
	except KeyError:
		pname = ""
	print "%s,%s,%s,%s" % (p[0], pname, p[1], points(p[1]))

