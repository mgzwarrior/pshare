'''
Author: Brandon Powers
Purpose:
    - Contains the unit tests for the
    'Twitter' class
'''

import unittest

class TestTwitter(unittest.TestCase):
    def setUp(self):
        print 'setUp()'

    def test_login(self):
        '''
        Tests login() & indirectly, known_user_auth()
        and first_time_auth() by checking the access
        token of 'self.auth'
        '''
        print 'test_login()'

    def test_get_tweepy_API(self):
        '''
        Tests get_tweepy_API & verify() indirectly
        '''
        print 'test_get_tweepy_API()'

    def test_statuses_to_tweets(self):
        print 'test_statuses_to_tweets()'

    def test_post(self):
        print 'test_post()'

    def test_delete(self):
        print 'test_delete()'
