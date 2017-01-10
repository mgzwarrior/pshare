'''
Object representing the actions specified 
with the -t flag for Twitter
'''

from tweet import Tweet
import tweepy
import os.path

# initializing authentication -- consumer info is hidden in local directory, not on GitHub for security purposes -- ask for use
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

class Twitter:
    def __init__(self, args):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.filename = 'twitter-access-token.txt'
        self.api = ''
        self.args = args
        
    def login(self):
        access_token_exists = os.path.isfile(self.filename)
        if access_token_exists: 
            self.known_user_auth()
        else:
            self.first_time_auth()

    def known_user_auth(self):
        # first line is TWITTER_ACCESS_KEY, second line is TWITTER_ACCESS_SECRET <-- reason for hardcoded indices
        with open(self.filename, 'r') as infile:
            access_token = infile.readlines()
            ACCESS_KEY = str(access_token[0]).rstrip('\n')
            ACCESS_SECRET = str(access_token[1])
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    def first_time_auth(self):
        try:
            print '**Initial authentication required for first-time user**'
            print '(1) Open the following URL in a web browser: ' + str(self.auth.get_authorization_url())
            print '(2) Authorize pshare to post to + read from your Twitter account'
            verifier = raw_input('(3) Input the access code Twitter redirects you to here: ')
            print '(4) Getting access token...'
            self.auth.get_access_token(verifier)
            print '(5) Storing access token information in file "twitter-access-token.txt" for future use'
            with open(self.filename, 'w') as outfile:
                outfile.write('{}\n{}'.format(self.auth.access_token, self.auth.access_token_secret))
        except tweepy.TweepError:
            print 'pshare.py: error: failed to get request token OR access token.'

    def get_tweepy_API(self):
        print 'Authenticating credentials...'
        self.api = tweepy.API(self.auth)
        self.verify()

    def verify(self):
        try:
            if self.api.verify_credentials():
                print 'Verified authentication credentials -- gained access to Twitter API'
        except tweepy.TweepError:
            print 'pshare.py: error: credentials are invalid: delete "twitter-access-token.txt" & re-authenticate'
            sys.exit(1)

    def read(self):
        statuses = []
        if self.args.cargs == 'home':
            statuses = self.api.home_timeline(count=self.args.number)
        elif self.args.cargs == 'user':
            statuses = self.api.user_timeline(count=self.args.number)
        tweets = self.statuses_to_tweets(statuses)
        print '\n**Top {} tweets on your timeline**\n'.format(str(self.args.number))
        for tweet in tweets:
            tweet.display(self.args.verbose)
    
    def statuses_to_tweets(self, statuses):
        tweets = []
        for status in statuses:
            name = str(status.user.name)
            screen_name = str(status.user.screen_name)
            text = status.text
            created_at = status.created_at
            id_num = status.id
            tweets.append(Tweet(name, screen_name, text, created_at, id_num))
        return tweets

    def post(self):
        try:
            # tweet media with cargs as text | tweet cargs as text, no media
            if not self.args.cargs == 'home' and self.args.media:
                self.api.update_with_media(self.args.media, self.args.cargs)
            elif not self.args.cargs == 'home':
                self.api.update_status(self.args.cargs)

            # tweet media with status file contents as text
            elif self.args.media and self.args.status:
                status = ''
                with open(self.args.status, 'r') as infile:
                    status = infile.read()
                self.api.update_with_media(self.args.media, status) 

            # only media file -- tweet media
            elif self.args.media:
                self.api.update_with_media(args.media)

            # only status file -- tweet contents
            elif self.args.status:
                status = ''
                with open(self.args.status, 'r') as infile:
                    status = infile.read()
                self.api.update_status(status)

            # prompt user -- no cargs, media, or status file
            else:
                status = raw_input('Enter tweet to post: ')
                self.api.update_status(status)
        
        except tweepy.TweepError:
            print 'pshare.py: error: tweet was over 140 characters OR encountered a post error' 
            sys.exit(1)

    def delete(self):
        try:
            self.api.destroy_status(self.args.cargs)
            print 'Deleted tweet with id #: {}'.format(str(self.args.cargs))
        except tweepy.TweepError:
            print 'pshare.py: error: tweet id # is invalid OR delete failed' 
            sys.exit(1)