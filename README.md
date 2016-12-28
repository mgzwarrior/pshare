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

###Usage:

    1. psh \<flags> \<command> \<command-args>
    2. flags:
        a. -f : apply command + command-args to Facebook
        b. -t : apply command + command-args to Twitter
    3. commands:
        a. help : print out documentation
        b. post : post args to platform(s)
        c. read : read from platform(s)
    4. command-args:
        a. plaintext
        b. filename, which contains the contents to be posted (need some way to specify, or check for extensions)
