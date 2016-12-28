## Description:

1. _pshare_ is a command-line interface (CLI) for social media sharing on Twitter and Facebook. The goal of pshare is to be *simple, lightweight, and easy to use* to do any type of CRUD-activity on the terminal.
2. The design of pshare is to be on top of Facebook and Twitter API wrappers, to allow them to do the heavy lifting of interacting directly with the API, which allows pshare to pick and choose the functions necessary and most commonly used to add to this project.
3. 
    pshare
    |
    |
    API Wrappers (tweepy, facepy)
    |
    |
    API (Facebook Graph API, Twitter API)

###TODO:

- List the features of pshare
    - post link / description to facebook (possibly img files)
    - post link / description to twitter (possibly img files)
- Come up with a design for the command ie. possible flags + args, list of platforms, etc. 
- Read up on platform API's for a post

- Stuff we're gunna need:
    - argparse module (python standard lib)
    - curl (unix library)
    - possible API's

- Use API wrappers tweepy & facepy OR manually work with API's? Figure out.
    - Pro of using wrappers:
        1. heavy lifting is done for us
        2. lets us use the functionality of these heavy API interaction wrappers to create a simple CLI that lets you post to BOTH in a single ocmmand, etc.
        3. So the power of pshare would be in it's simplicity & combination of social medias. ALSO, it would be a layer on top of these wrappers, so very high level.
        4. Easier/faster to develop
