#!/opt/local/bin/python2.7

from bs4 import BeautifulSoup
import requests
import datetime

URL = 'http://baseball.fantasysports.yahoo.com/b1/58506/team'
cookie_value = open('cook2.txt').read()
headers = {'Cookie' : cookie_value}

NUMTEAMS = 20
dt = datetime.date(2013,3,31)

def convert_to_num(stri):
	if(stri == '-'):
		return 0
	return float(stri)

while dt < datetime.date.today():
#for team in range(1,NUMTEAMS+1):
	for team in range(7,8):

		DATESTR = dt.isoformat()
		payload = {'date': DATESTR, 'mid': team, 'week': 1}
		r = requests.get(URL, params=payload, headers=headers)
		soup = BeautifulSoup(r.text)

		batting_team_totals = soup.find_all('div', 'ptstotal')[0].find_all('li')
		AB = int(convert_to_num(batting_team_totals[1].text))
		H  = int(convert_to_num(batting_team_totals[2].text))
		DB = int(convert_to_num(batting_team_totals[3].text))
		TP = int(convert_to_num(batting_team_totals[4].text))
		HR = int(convert_to_num(batting_team_totals[5].text))
		SB = int(convert_to_num(batting_team_totals[6].text))
		CS = int(convert_to_num(batting_team_totals[7].text))
		BB = int(convert_to_num(batting_team_totals[8].text))

		pitching_team_totals = soup.find_all('div', 'ptstotal')[1].find_all('li')
		IP  = float(convert_to_num(pitching_team_totals[0].text))
		HRA = int(convert_to_num(pitching_team_totals[1].text))
		BBA = int(convert_to_num(pitching_team_totals[2].text))
		K   = int(convert_to_num(pitching_team_totals[3].text))

		print DATESTR, team, AB, H, DB, TP, HR, SB, CS, BB, IP, HRA, BBA, K 

	dt += datetime.timedelta(1)
