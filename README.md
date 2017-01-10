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

    1. psh <flags> <command> <cargs | cflags>
    2. flags:
        a. -f : apply command + command-args to Facebook
        b. -t : apply command + command-args to Twitter
    3. commands:
        a. post : post args to platform(s)
        b. read : read from platform(s)
        b. del : del from platform(s)
    4. cargs:
        a. read : home | user (default: home)
        b. post : "str" | "" (default: home, when used w post, prompts user to type in status)
        c. del : 123456 (id_num of tweet)
    5. cflags:
        a. post : -m "media-filename.jpg" | -s "status-filename.txt"
        b. read : -n 5 (output 5 tweets) | -v (display more info per tweet)

    6. Examples:

        psh -t post (prompt user to enter status)
        psh -t post "tweet" (tweet cargs)
        psh -t post -s "file.txt" (tweet contents of file.txt)
        psh -t post -m "media.jpg" -s "file.txt" (tweet media.jpg with contents of file.txt as status)
        psh -t post "media-text" -m "media.jpg"
        psh -t read (default: home feed w 10 tweets)
        psh -t read user -v -n 5 (user feed w 5 tweets & verbose info)
        psh -t del 81067 (delete tweet w id_num 81067)

## Description:

1. _pshare_ is a command-line interface (CLI) for social media sharing on Twitter and Facebook. The goal of pshare is to be *simple, lightweight, and easy to use* to do any type of CRUD-activity on the terminal.
2. The design of pshare is to be on top of Facebook and Twitter API wrappers, to allow them to do the heavy lifting of interacting directly with the API, which allows pshare to pick and choose the functions necessary and most commonly used to add to this project.
3. pshare -- API Wrappers (tweepy, facepy) -- API (Facebook Graph API, Twitter API)

###TODO:

    1. Describe the overall goal of pshare -- why use it?
        - to provide an intuitive, straight-forward CLI to fb + twitter
    2. What are the use cases of pshare?
        - post, read, del (only a subset of API functionality to accomplish core tasks)
    3. How are we going to implement above use cases?
        - tweepy + facepy + custom functionality
    4. Design the specifics of the application: possible classes, modules (argparse), examples of usage, dependencies, etc..
        - usage: 
            psh -f post <post-description>... (post to fb)
            psh -ft read (output twitter feed + fb timeline)
        - dependencies:
            tweepy
            facepy
    5. Create two different install / build routes:
        - git clone https://github.com/mgzwarrior/pshare.git
        - pip install pshare
