# UoM Telstra M2M Challenge
#HTML Information Extractor
#twendr.com
# James Cocks, Chin Wai Ng
################################################################
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

# Authentication keys required to access twitter API 1.1
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "4xxsfLCqmbzxhwdp6wIg2w"
CONSUMER_SECRET = "6KwoEYXyoAeGGOr0HzADbF2HJIVMZujjAXH6yL79mc"

OAUTH_TOKEN = "108416289-9gidVFdSYJiFqThWX39fr8zfwwR2xYsFg7iVSPzW"
OAUTH_TOKEN_SECRET = "7Cq57yiKq8VQ8LOMqxdUoEEIulfIJS2uSX3eLttu1A"


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth


oauth = get_oauth()
# WOEID 1 for the global tweet trends
result = requests.get(url="https://api.twitter.com/1.1/trends/place.json?id=1", auth=oauth)
trend_result = result.json()

    


