#!/usr/bin/python

# takes as input the output from parse_st_data.py
# outputs the lines of the hitters in a more interesting and readable format

import sys
import csv

for line in csv.reader(sys.stdin.readlines()):
	if int(line[2]) > 0:
		# batter
		id, name = line[0], line[1]
		(ab, h, dbl, tpl, hr, sb, cs, bb) = map(float, (line[2:10]))
		pts = float(line[15])
		pa = ab+bb
		ba = h/ab
		obp = (h+bb)/pa
		slg = (h+dbl+2*tpl+3*hr)/ab
		ops = obp + slg
		print "%4d %.3f %.3f %.3f %5.1f %6.3f %20s " % (int(pa), ba, obp, slg, pts, pts/pa, name)
