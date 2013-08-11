#!/usr/bin/python

import sys
import bs4
import requests
import datetime

# constants/etc
URL = 'http://baseball.fantasysports.yahoo.com/b1/57874/team'
with open('cook2.txt') as f:
	cookie_value = f.read()
headers = {'Cookie' : cookie_value}

# configuration
STARTTEAM = int(sys.argv[1])
NUMTEAMS = int(sys.argv[2])
STARTDATE = datetime.date(2013,3,31)

# funcs to convert the string formatted stats to numeric types
def convert_to_int(stri):
	return (int(stri) if (stri != '-') else 0)

def convert_to_float(stri):
	return (float(stri) if (stri != '-') else 0.0)

# a generator to yield the dates (since range() doesn't work on dates)
def dates():
	dt = STARTDATE
	while dt < datetime.date.today():
		yield dt
		dt += datetime.timedelta(1)

# OK, here we go, looping on date, then team
for dt in dates():
	for team in range(STARTTEAM,NUMTEAMS+STARTTEAM):

		datestr = dt.isoformat()
		params = {'date': datestr, 'mid': team, 'week': 1}
		r = requests.get(URL, params=params, headers=headers)
		if r.status_code != 200:
			sys.stderr.write(r.text)
			raise Exception("Error from Yahoo", r.status_code)
		soup = bs4.BeautifulSoup(r.text)

		# this will get the two team totals lines; pull them aside 
		#   to avoid running find_all/find twice
		totals_lines = soup.find_all('div', 'ptstotal')

		batting_team_totals = totals_lines[0].find_all('li')
		AB = convert_to_int(batting_team_totals[1].text)
		H  = convert_to_int(batting_team_totals[2].text)
		DB = convert_to_int(batting_team_totals[3].text)
		TP = convert_to_int(batting_team_totals[4].text)
		HR = convert_to_int(batting_team_totals[5].text)
		SB = convert_to_int(batting_team_totals[6].text)
		CS = convert_to_int(batting_team_totals[7].text)
		BB = convert_to_int(batting_team_totals[8].text)

		pitching_team_totals = totals_lines[1].find_all('li')
		IP  = convert_to_float(pitching_team_totals[0].text)
		HRA = convert_to_int(pitching_team_totals[1].text)
		BBA = convert_to_int(pitching_team_totals[2].text)
		K   = convert_to_int(pitching_team_totals[3].text)

		print datestr, team, AB, H, DB, TP, HR, SB, CS, BB, IP, HRA, BBA, K 

