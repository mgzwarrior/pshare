##pshare
__Allows you to interact with your social media (Twitter + Facebook) through the command-line.__

Suppose you'd like to:

1. Read your timeline on both Twitter & Facebook:
    
    ```
    psh -tf read
    ```
2. Share a blog post on Facebook:
    
    ```
    psh -f post "Check out my latest post at: https://brandon-powers.github.io/blog/why-computer-science"
    ```
3. Upload a picture with a description on Twitter (-m "file.jpg" specifies the media filename):
    
    ```
    psh -t post "This pic is something else!" -m "media-file.jpg"
    ```
4. Delete your most recent tweet ('user' reads your tweets, -n 1 says read 1 tweet, -v adds tweet id to the output):

    ```
    psh -t read user -n 1 -v
    # copy the tweet id from stdout
    psh -t del <tweet_id>
    ```

Check out the docs below for additional usage information.

##Dependencies:

First, pshare is written in Python 2.7, so your interpreter must be version 2.7.

Second, it depends on the following API wrappers that you'll need to install:

1. tweepy (which can be found here: https://github.com/tweepy/tweepy)
    - Using PyPI: 
        ```
        pip install tweepy
        ```

    - Manual setup:
        ```
        git clone https://github.com/tweepy/tweepy.git
        cd tweepy
        python setup.py install
        ```

2. facepy

##Installation

The easiest way to install pshare is using PyPI (TODO -- not implemented yet):
    
    pip install pshare

Or you can manually install it:
    
    git clone https://github.com/mgzwarrior/pshare
    cd src/
    psh ...

##Usage:

1. read

    - Twitter:

        ```
        psh -t read [cargs] [cflags]
        cargs = [home, user] (defaults to home -- which feed to read)
        cflags = [-n #] [-v] (print out n posts, print extra information per post)
        ```

    - Facebook:

        ```
        psh -f read [cflags]
        cflags = same as above
        ```

    Note: only difference is cargs does NOT affect the facebook read command
    but they can be used together, it simply has no effect on FB, only twitter.

2. post

    - Twitter & Facebook:

        ```
        psh -tf post [cargs] [cflags]
        cargs = ["description/post"]
        cflags = [-m "media.jpg"] [-s "status.txt"]
        ```
        
3. del

    - Twitter & Facebook:

        ```
        psh -t del [cargs]
        psh -f del [cargs]
        cargs = [id_number]
        id_number = id of tweet or facebook post to be deleted (can be found with read command)
        ```

4. Examples

        psh -tf post (prompt user to enter status)
        psh -tf post "description" (post "description")
        psh -tf post -s "file.txt" (post contents of file.txt)
        psh -tf post -m "media.jpg" -s "file.txt" (post media.jpg with contents of file.txt as status)
        psh -tf post "description" -m "media.jpg" (post media.jpg with "description") 
        
        psh -t read (default: home feed with 10 tweets)
        psh -t read user -v -n 5 (user feed with 5 tweets & verbose info)
        psh -f read (default: 10 posts)
        psh -f read -v -n 5 (display 5 posts with verbose info)
        
        psh [-t | -f] del 81067 (delete tweet/post with id_num 81067)

## Description:

1. _pshare_ is a command-line interface (CLI) for social media sharing on Twitter and Facebook. The goal of pshare is to be *simple, lightweight, and easy to use* to do any type of CRUD-activity on the terminal.
2. The design of pshare is to be on top of Facebook and Twitter API wrappers, to allow them to do the heavy lifting of interacting directly with the API, which allows pshare to pick and choose the functions necessary and most commonly used to add to this project.
3. pshare -- API Wrappers (tweepy, facepy) -- API (Facebook Graph API, Twitter API)
