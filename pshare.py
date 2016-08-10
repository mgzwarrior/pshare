'''
Authors: Brandon Powers & Matt Grant
'''

import os
import argparse

def post(content):
    # Replace whitespace with %20 for url
    content = content.replace(' ', '%20');

    # Using maker & ifttt to post status to facebook -- work in progress, requires manual sign up 
    post_url = 'https://maker.ifttt.com/trigger/post_status_fb/with/key/h9r8MaI_aGqrQjLUOArRf0Y1zeNQf1H-_ttKD_sc6R1?value1=' + content
    os.system('curl -X POST ' + post_url)
    print ''

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument('post', help='type in the content of your post')

    # Get command-line arguments
    args = parser.parse_args()

    # Execute command
    post(args.post)

if __name__ == '__main__':
    main()
