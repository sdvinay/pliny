#!/usr/bin/python

import sys
import requests # http://docs.python-requests.org/en/latest/
import datetime
import argparse

import parse_team_totals # parsing the stats from the HTML is in our local module

# constants/etc
DESCRIPTION='Fetch and parse daily team total stats.  Play with the start_team and num_teams parameters to divide-and-conquer with a few parallel instances.'
#LEAGUE=28858 # weights two
LEAGUE=41702 # super lounge weights 
URL = 'http://baseball.fantasysports.yahoo.com/b1/' + str(LEAGUE) + '/team'
with open('fixtures/private/yahoo_auth_cookie.txt') as f:
	cookie_value = f.read()
headers = {'Cookie' : cookie_value, "Accept-Encoding": "gzip,deflate,sdch", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
OUTPUT_DELIMITER=' '

# configuration
parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('start_team', type=int, help="Team number of first team")
parser.add_argument('num_teams', type=int, help="Number of teams to fetch")
parser.add_argument('start_date', help="Start Date, as YYYY-MM-DD")
args = parser.parse_args()
STARTTEAM = args.start_team
NUMTEAMS = args.num_teams
STARTDATE = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")

# a generator to yield the dates (since range() doesn't work on dates)
def dates():
	dt = STARTDATE.date()
	while dt <= datetime.date.today():
		yield dt
		dt += datetime.timedelta(1)

# OK, here we go, looping on date, then team
for dt in dates():
	for team in range(STARTTEAM,NUMTEAMS+STARTTEAM):
		# construct the HTTP request and pass the response body to our parser
		datestr = dt.isoformat()
		params = {'date': datestr, 'mid': team, 'week': 1}
		r = requests.get(URL, params=params, headers=headers)
		if r.status_code != 200:
			sys.stderr.write(r.text)
			raise Exception("Error from Yahoo", r.status_code)
		team_totals = parse_team_totals.parse_team_totals(r.text)
		output_fields = (datestr, team) + team_totals # add our metadata

		print OUTPUT_DELIMITER.join([str(x) for x in output_fields])


