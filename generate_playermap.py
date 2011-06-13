#!/usr/bin/python

import sys

# put the player names in a map
player_name = dict()

for player_line in open('data/players.txt', 'r').readlines():
	if (player_line.startswith("m|")):
#		print player_line
		player_data = player_line.split("|")
		pname = "%s %s" % (player_data[3], player_data[4])
		pnum = player_data[1]
		player_name[pnum] = pname

f = open('data/stattracker_data.html', 'r')
player_line = filter(lambda str: str.startswith("players^"), f.readlines())[0]
player_list = player_line.split("^")[1:]
for player_data_line in player_list:
	#print player_data_line
	player_data = player_data_line.split("|")
	pnum = player_data[0]
	player_name[pnum] = player_data[1]
	#print player_name
	#	print pnum, player_data[1]

outfile = open('data/playermap.txt', 'w')
for pnum in player_name:
	outfile.write("%s,%s\n" % (pnum, player_name[pnum]))

