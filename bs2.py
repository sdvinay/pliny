#!/usr/bin/python

import sys
import bs4 # BeautifulSoup http://www.crummy.com/software/BeautifulSoup/

# funcs to convert the string formatted stats to numeric types
def convert_to_int(stri):
	return (int(stri) if (stri != '-') else 0)

def convert_to_float(stri):
	return (float(stri) if (stri != '-') else 0.0)


with open('t1.html') as f:
	html = f.read()

soup = bs4.BeautifulSoup(html)

# The two team stats totals (batting and pitching) are in:
#    <div class="sum ptstotal">
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

print "DATE", "team", AB, H, DB, TP, HR, SB, CS, BB, bat_pts, IP, HRA, BBA, K, pit_pts

