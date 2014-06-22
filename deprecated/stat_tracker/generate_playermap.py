#!/usr/bin/python

import sys

# put the player names in a map
player_names = dict()

for player_line in open('data/players.txt', 'r').readlines():
	if (player_line.startswith("m|")):
#		print player_line
		player_data = player_line.split("|")
		pname = "%s %s" % (player_data[3], player_data[4])
		pnum = player_data[1]
		player_names[pnum] = pname

f = open('data/stattracker_data.html', 'r')
line_with_all_player_data = filter(lambda str: str.startswith("players^"), f.readlines())[0]
player_data_list = line_with_all_player_data.split("^")[1:]
for player_data_line in player_data_list:
	#print player_data_line
	player_data = player_data_line.split("|")
	pnum = player_data[0]
	player_names[pnum] = player_data[1]
	#print player_names
	#	print pnum, player_data[1]

outfile = open('data/playermap.txt', 'w')
for pnum in player_names:
	outfile.write("%s,%s\n" % (pnum, player_names[pnum]))

