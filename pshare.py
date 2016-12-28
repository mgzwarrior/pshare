'''
Authors: Brandon Powers & Matt Grant
'''

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('post', help='type in the content of your post')
    args = parser.parse_args()
    print args.post

if __name__ == '__main__':
    main()
