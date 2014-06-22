#/bin/sh

wget 'http://aud13.sports.sp2.yahoo.com/mlb/players.txt' --output-document=data/players.txt

# This assumes a file called yahoo_auth_cookies.txt, which includes the yahoo
# auth cookie in a format that can be consumed directly as a header.  Specifically,
#   Cookie:Y=<value>; T=<value>
# For obvious reasons, I'm not checking in the file yahoo_auth_cookies.txt
# Without this cookies file, you won't be able to download stattracker data
YAHOO_AUTH_COOKIE_HEADER=$(cat yahoo_auth_cookies.txt)

wget --header=${YAHOO_AUTH_COOKIE_HEADER} \
	--output-document=data/stattracker_data.html \
	'http://baseball.fantasysports.yahoo.com/b1/stattracker_data?lid=18735&type=mlb'



