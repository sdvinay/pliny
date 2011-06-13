#/bin/sh

wget 'http://aud13.sports.sp2.yahoo.com/mlb/players.txt' --output-document=data/players.txt

YAHOO_AUTH_COOKIE_HEADER=$(cat yahoo_auth_cookies.txt)

wget --header=${YAHOO_AUTH_COOKIE_HEADER} \
	--output-document=data/stattracker_data.html \
	'http://baseball.fantasysports.yahoo.com/b1/stattracker_data?lid=18735&type=mlb'



