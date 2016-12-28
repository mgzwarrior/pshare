'''
Authors: Brandon Powers & Matt Grant
'''

import argparse

parser = argparse.ArgumentParser(description='post + read + del to and from Facebook and/or Twitter')
parser.add_argument('-f', '--facebook', action='store_true',
                    help='apply <command> <command-args> to Facebook')
parser.add_argument('-t', '--twitter', action='store_true',
                    help='apply <command> <command-args> to Twitter')
args = parser.parse_args()

if args.facebook:
    print 'apply to Facebook'
if args.twitter:
    print 'apply to Twitter'
