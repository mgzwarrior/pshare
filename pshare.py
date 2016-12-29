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

# initializing authentication -- consumer info is hidden in local directory, not on GitHub for security purposes -- ask for use
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET);

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

def init_twitter():
    try:
        filename = 'twitter-access-token.txt'
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
    
def auth_twitter():
    # first line is ACCESS_KEY, second line is ACCESS_SECRET <-- reason for hardcoded indices
    filename = 'twitter-access-token.txt'
    with open(filename, 'r') as infile:
        access_token = infile.readlines()
        ACCESS_KEY = str(access_token[0]).rstrip('\n')
        ACCESS_SECRET = str(access_token[1])
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

def verify_twitter(api):
    try:
        if api.verify_credentials():
            print 'Verified authentication credentials -- gained access to Twitter API'
    except tweepy.TweepError:
        print 'pshare.py: error: credentials are invalid: delete "twitter-access-token.txt" & re-authenticate'
        sys.exit(1)


def init_facebook():
    print 'init_facebook()'

def auth_facebook():
    print 'auth_facebook()'

def verify_facebook():
    print 'verify_facebook()'

def main():
    if args.twitter:
        filename = 'twitter-access-token.txt'
        access_token_exists = os.path.isfile(filename)
        if access_token_exists:
            auth_twitter()
        else:
            init_twitter()
        
        print 'Authenticating credentials...'
        api = tweepy.API(auth)
        verify_twitter(api)
        
        # Defaults to posting a tweet (despite command) for testing purposes
        api.update_status(raw_input('Enter tweet: '))
    
    if args.facebook:
        # Facebook OAuth not implemented yet
        print 'called with -f flag for facebook'
    
    # check positional argument <command>
    if args.command == 'read':
        print 'read'
    elif args.command == 'post':
        print 'post'
    else:
        print 'del'

if __name__ == '__main__':
    main()
