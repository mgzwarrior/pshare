'''
Authors: Brandon Powers & Matt Grant
'''

import sys
import argparse
import tweepy
import os.path

# Disables two warnings when pshare is run
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

CONSUMER_KEY = 'xopCIjkuJk5FJupf653EAI9Am'
CONSUMER_SECRET = 'X7BVFS7GCYIUzsvQE6JuiFTnFnPPvDy954UUVb6HxOF0MAXXlH'
ACCESS_KEY = ''
ACCESS_SECRET = ''

# initializing parser 
parser = argparse.ArgumentParser(description='post + read + del to and from Facebook and/or Twitter')
parser.add_argument('-f', '--facebook', action='store_true',
                    help='apply <command> <command-args> to Facebook')
parser.add_argument('-t', '--twitter', action='store_true',
                    help='apply <command> <command-args> to Twitter')
parser.add_argument('command', type=str, choices=['read', 'post', 'del'], help='command to execute')
args = parser.parse_args()

# check optional flag args
if args.facebook:
    print 'apply to Facebook'

if args.twitter:
    filename = 'twitter-access-token.txt'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET);
    
    # two possible states: registered or not
    if os.path.isfile(filename):
        with open(filename, 'r') as infile:
            access_token = infile.readlines()
            ACCESS_KEY = str(access_token[0]).rstrip('\n') # first line is key -- reason for hardcoded index
            ACCESS_SECRET = str(access_token[1]) # second line is secret -- "
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    else:
        try:
            print '**Initial authentication required for first-time user**'
            print '(1) Open the following URL in a web browser: ' + str(auth.get_authorization_url())
            print '(2) Authorize pshare to post to + read from your Twitter account'
            verifier = raw_input('(3) Input the access code Twitter redirects you to here: ')
            print '(4) Getting access token...'
            auth.get_access_token(verifier)
            print '(5) Storing access token information in file "twitter-access-token.txt" for future use'
            with open(filename, 'w') as outfile:
                outfile.write('{}\n{}'.format(auth.access_token, auth.access_token_secret))
        except tweepy.TweepError:
            print 'pshare.py: error: failed to get request token OR access token.'

    print 'Authenticating credentials...'
    api = tweepy.API(auth)
    try:
        if api.verify_credentials():
            print 'Verified authentication credentials -- gained access to Twitter API'
    except tweepy.TweepError:
        print 'pshare.py: error: credentials are invalid: delete "twitter-access-token.txt" & re-authenticate'
        sys.exit(1)
    api.update_status(raw_input('Enter status: '))

# check positional argument <command>
if args.command == 'read':
    print 'read'
elif args.command == 'post':
    print 'post'
else:
    print 'del'
