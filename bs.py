#!/usr/bin/python

import sys
import bs4
import requests
import datetime

URL = 'http://baseball.fantasysports.yahoo.com/b1/57874/team'
cookie_value = open('cook2.txt').read()
headers = {'Cookie' : cookie_value}

STARTTEAM = int(sys.argv[1])
NUMTEAMS = int(sys.argv[2])
dt = datetime.date(2013,3,31)

def convert_to_int(stri):
	if(stri == '-'):
		return 0
	return int(stri)

def convert_to_float(stri):
	if(stri == '-'):
		return 0
	return float(stri)

while dt < datetime.date.today():
	for team in range(STARTTEAM,NUMTEAMS+STARTTEAM):

		DATESTR = dt.isoformat()
		payload = {'date': DATESTR, 'mid': team, 'week': 1}
		r = requests.get(URL, params=payload, headers=headers)
		soup = bs4.BeautifulSoup(r.text)

		batting_team_totals = soup.find_all('div', 'ptstotal')[0].find_all('li')
		AB = convert_to_int(batting_team_totals[1].text)
		H  = convert_to_int(batting_team_totals[2].text)
		DB = convert_to_int(batting_team_totals[3].text)
		TP = convert_to_int(batting_team_totals[4].text)
		HR = convert_to_int(batting_team_totals[5].text)
		SB = convert_to_int(batting_team_totals[6].text)
		CS = convert_to_int(batting_team_totals[7].text)
		BB = convert_to_int(batting_team_totals[8].text)

		pitching_team_totals = soup.find_all('div', 'ptstotal')[1].find_all('li')
		IP  = convert_to_float(pitching_team_totals[0].text)
		HRA = convert_to_int(pitching_team_totals[1].text)
		BBA = convert_to_int(pitching_team_totals[2].text)
		K   = convert_to_int(pitching_team_totals[3].text)

		print DATESTR, team, AB, H, DB, TP, HR, SB, CS, BB, IP, HRA, BBA, K 

	dt += datetime.timedelta(1)
