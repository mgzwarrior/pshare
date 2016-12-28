'''
Authors: Brandon Powers & Matt Grant
'''

import argparse

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
    print 'apply to Twitter'

# check positional argument <command>
if args.command == 'read':
    print 'read'
elif args.command == 'post':
    print 'post'
else:
    print 'del'
