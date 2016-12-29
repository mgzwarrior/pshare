'''
Authors: Brandon Powers & Matt Grant
'''
# TODO: Twitter actions:
#           - post tweet (both txt + media files w/ txt): 
#               - psh -t post -m "dog.jpg" -s "status/description.txt"
#               - psh -t post -s "status/description.txt"
#               - psh -t post "hey there twitter!"
#               - psh -t post (will prompt the user to enter status into stdin)
#           - read tweet(s): 
#               - psh -t read -n 40 (output twitter feed (40 statuses))
#               - psh -t read -v (output twitter feed w extra info per tweet (default: 10 statuses))
#               - psh -t read (output [home] twitter feed (default: 10 statuses))
#               - psh -t read home (output [home] twitter feed (default: 10 statuses))
#               - psh -t read user (output [user] twitter feed (default: 10 statuses))
#               - psh -t read user -v -n 5 (output [user] twitter feed w extra info (5 statuses))
#           - del tweet(s)
#               - psh -t del <id_num> (delete tweet with id_num)

from tweet import Tweet
import sys
import argparse
import tweepy
import os.path

# Disables two warnings when pshare is run
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# initializing authentication -- consumer info is hidden in local directory, not on GitHub for security purposes -- ask for use

TWITTER_CONSUMER_KEY = 'xopCIjkuJk5FJupf653EAI9Am'
TWITTER_CONSUMER_SECRET = 'X7BVFS7GCYIUzsvQE6JuiFTnFnPPvDy954UUVb6HxOF0MAXXlH'
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)

TWITTER_ACCESS_KEY = ''
TWITTER_ACCESS_SECRET = ''

# initializing parser 
parser = argparse.ArgumentParser(description='post + read + del to and from Facebook and/or Twitter')
parser.add_argument('-f', '--facebook', action='store_true',
                    help='apply <command> <command-args> to Facebook')
parser.add_argument('-t', '--twitter', action='store_true',
                    help='apply <command> <command-args> to Twitter')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='display extra information')
parser.add_argument('-n', '--number', type=int, default=10,
                    help='amount of tweets to be displayed')
parser.add_argument('-m', '--media', type=str, default='',
                    help='name of media file to be posted')
parser.add_argument('-s', '--status', type=str, default='',
                    help='name of text file to be posted')
parser.add_argument('command', type=str, choices=['read', 'post', 'del'], help='command to execute')
parser.add_argument('cargs', type=str, nargs='?', default='home', help='args for previous command')
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
    # first line is TWITTER_ACCESS_KEY, second line is TWITTER_ACCESS_SECRET <-- reason for hardcoded indices
    filename = 'twitter-access-token.txt'
    with open(filename, 'r') as infile:
        access_token = infile.readlines()
        TWITTER_ACCESS_KEY = str(access_token[0]).rstrip('\n')
        TWITTER_ACCESS_SECRET = str(access_token[1])
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)

def verify_twitter(api):
    try:
        if api.verify_credentials():
            print 'Verified authentication credentials -- gained access to Twitter API'
    except tweepy.TweepError:
        print 'pshare.py: error: credentials are invalid: delete "twitter-access-token.txt" & re-authenticate'
        sys.exit(1)

def statuses_to_tweets(statuses):
    tweets = []
    for status in statuses:
        name = str(status.user.name)
        screen_name = str(status.user.screen_name)
        text = status.text
        created_at = status.created_at
        id_num = status.id
        tweets.append(Tweet(name, screen_name, text, created_at, id_num))
    return tweets

def read_twitter(api):
    statuses = []
    if args.cargs == 'home':
        statuses = api.home_timeline(count=args.number)
    elif args.cargs == 'user':
        statuses = api.user_timeline(count=args.number)
    tweets = statuses_to_tweets(statuses)
    print '\n**Top {} tweets on your timeline**\n'.format(str(args.number))
    for tweet in tweets:
        tweet.display(args.verbose)

def post_twitter(api):
    if not args.cargs == 'home':
        api.update_status(args.cargs)
    elif args.media and args.status:
        status = ''
        with open(args.status, 'r') as infile:
            status = infile.read()
        api.update_with_media(args.media, status) 
    elif args.media:
        api.update_with_media(args.media)
    elif args.status:
        status = ''
        with open(args.status, 'r') as infile:
            status = infile.read()
        api.update_status(status)
    else:
        status = raw_input('Enter tweet to post: ')
        api.update_status(status)

def del_twitter(api):
    try:
        api.destroy_status(args.cargs)
        print 'Deleted tweet with id #: {}'.format(str(args.cargs))
    except tweepy.TweepError:
        print 'pshare.py: error: tweet id # is invalid OR delete failed' 
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
        
        if args.command == 'read':
            read_twitter(api)
        elif args.command == 'post':
            post_twitter(api)
        else:
            del_twitter(api)
    
    if args.facebook:
        # Facebook OAuth not implemented yet
        print 'called with -f flag for facebook'
    
if __name__ == '__main__':
    main()
