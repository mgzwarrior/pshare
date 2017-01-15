'''
Author: Brandon Powers
Purpose:
    - Contains the unit tests for the
    'Twitter' class
'''

import unittest
from twitter import Twitter
from argparse import Namespace

# Disables two warnings when pshare is run
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

class TestTwitter(unittest.TestCase):
    def setUp(self):
        # simulate "psh -t read" command args
        args = Namespace(cargs='home', command='read', facebook=False, media='', number=10, status='', twitter=True, verbose=False)
        self.t = Twitter(args)
        print 'setUp()'

    def test_login(self):
        '''
        Tests login() & indirectly, known_user_auth()
        and first_time_auth() by checking the access
        token of 'self.auth'
        '''
        self.t.login()
        
        # read in access token from 'twitter-access-token.txt'
        with open('twitter-access-token.txt', 'r') as infile:
            content = infile.readlines()
        access_token = content[0].rstrip()
        access_token_secret = content[1].rstrip()
        self.assertEqual(self.t.auth.access_token, access_token)
        self.assertEqual(self.t.auth.access_token_secret, access_token_secret)

    #def test_get_tweepy_API(self):
        '''
        Tests get_tweepy_API & verify() indirectly
        '''

    #def test_statuses_to_tweets(self):

    #def test_post(self):

    #def test_delete(self):

if __name__ == '__main__':
    unittest.main()
