#!/usr/bin/python

import sys
import bs4 # BeautifulSoup http://www.crummy.com/software/BeautifulSoup/
import requests # http://docs.python-requests.org/en/latest/
import datetime

# constants/etc
#LEAGUE=28858 # weights two
LEAGUE=41702 # super lounge weights 
URL = 'http://baseball.fantasysports.yahoo.com/b1/' + str(LEAGUE) + '/team'
with open('cook2.txt') as f:
	cookie_value = f.read()
headers = {'Cookie' : cookie_value, "Accept-Encoding": "gzip,deflate,sdch", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

# configuration
STARTTEAM = int(sys.argv[1])
NUMTEAMS = int(sys.argv[2])
STARTDATE = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d")

# funcs to convert the string formatted stats to numeric types
def convert_to_int(stri):
	return (int(stri) if (stri != '-') else 0)

def convert_to_float(stri):
	return (float(stri) if (stri != '-') else 0.0)

# a generator to yield the dates (since range() doesn't work on dates)
def dates():
	dt = STARTDATE.date()
	while dt <= datetime.date.today():
		yield dt
		dt += datetime.timedelta(1)

# OK, here we go, looping on date, then team
for dt in dates():
	for team in range(STARTTEAM,NUMTEAMS+STARTTEAM):
		# construct the HTTP request and then pull it into Soup
		datestr = dt.isoformat()
		params = {'date': datestr, 'mid': team, 'week': 1}
		r = requests.get(URL, params=params, headers=headers)
		if r.status_code != 200:
			sys.stderr.write(r.text)
			raise Exception("Error from Yahoo", r.status_code)
		soup = bs4.BeautifulSoup(r.text)

		# The two team stats totals (batting and pitching) are in tfoots
		# BeautifulSoup makes it easy to grab those into an array to pull from
		footers = soup.find_all('tfoot')

		batting_team_totals = footers[0].find_all('td')
		AB = convert_to_int(batting_team_totals[3].text)
		H  = convert_to_int(batting_team_totals[4].text)
		DB = convert_to_int(batting_team_totals[5].text)
		TP = convert_to_int(batting_team_totals[6].text)
		HR = convert_to_int(batting_team_totals[7].text)
		SB = convert_to_int(batting_team_totals[8].text)
		CS = convert_to_int(batting_team_totals[9].text)
		BB = convert_to_int(batting_team_totals[10].text)
		bat_pts = convert_to_float(batting_team_totals[11].text)

		pitching_team_totals = footers[1].find_all('td')
		IP  = convert_to_float(pitching_team_totals[2].text)
		HRA = convert_to_int(pitching_team_totals[3].text)
		BBA = convert_to_int(pitching_team_totals[4].text)
		K   = convert_to_int(pitching_team_totals[5].text)
		pit_pts = convert_to_float(pitching_team_totals[6].text)

		print datestr, team, AB, H, DB, TP, HR, SB, CS, BB, IP, HRA, BBA, K, bat_pts, pit_pts, bat_pts+pit_pts


