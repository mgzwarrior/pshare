'''
Authors: Brandon Powers & Matt Grant
'''

from twitter import Twitter
import argparse

# Disables two warnings when pshare is run
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# initializing parser 
# usage: psh <flags> <command> <cargs | cflags>
parser = argparse.ArgumentParser(description='post + read + del to and from Facebook and/or Twitter',
                                prog='pshare', usage='%(prog)s <flags> <command> <cargs | cflags>',
                                epilog='See documentation at https://github.com/mgzwarrior/pshare for more help.')
flags = parser.add_argument_group('flags')
flags.add_argument('-f', '--facebook', action='store_true',
                    help='apply <command> to Facebook')
flags.add_argument('-t', '--twitter', action='store_true',
                    help='apply <command> to Twitter')
parser.add_argument('command', type=str, choices=['read', 'post', 'del'], 
                    help='command to execute')
parser.add_argument('cargs', type=str, nargs='?', default='home', 
                    help='command args')
cflags = parser.add_argument_group('cflags')
cflags.add_argument('-v', '--verbose', action='store_true',
                    help='display extra information')
cflags.add_argument('-n', '--number', type=int, default=10,
                    help='amount of tweets to be displayed')
cflags.add_argument('-m', '--media', type=str, default='',
                    help='name of media file to be posted')
cflags.add_argument('-s', '--status', type=str, default='',
                    help='name of text file to be posted')
args = parser.parse_args()

def init_facebook():
    print 'init_facebook()'

def auth_facebook():
    print 'auth_facebook()'

def verify_facebook():
    print 'verify_facebook()'

def main():
    if args.twitter:
        t = Twitter(args)
        t.login()
        t.get_tweepy_API()
        if args.command == 'read':
            t.read()
        elif args.command == 'post':
            t.post()
        else:
            t.delete()

    if args.facebook:
        # TODO: implement Facebook class OR functions
        print 'Facebook flag -f specified'
    
if __name__ == '__main__':
    main()
