#!/usr/bin/python

# takes as input the output from parse_st_data.py
# outputs the lines of the pitchers in a more interesting and readable format

import sys
import csv

for line in csv.reader(sys.stdin.readlines()):
	if int(line[11]) > 0:
		# pitcher
		id, name = line[0], line[1]
		(ipout, hr, bb, k) = map(int, (line[11:15]))
		pts = float(line[15])
		ip = float(ipout)/3
		plus_minus = k - bb - 4.5*hr
		print "%5.1f %5.1f %6.3f %3d %20s " % (ip, pts, pts/ip, plus_minus, name)

