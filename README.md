## Description:

1. _pshare_ is a command-line interface (CLI) for social media sharing on Twitter and Facebook. The goal of pshare is to be *simple, lightweight, and easy to use* to do any type of CRUD-activity on the terminal.
2. The design of pshare is to be on top of Facebook and Twitter API wrappers, to allow them to do the heavy lifting of interacting directly with the API, which allows pshare to pick and choose the functions necessary and most commonly used to add to this project.
3. 
    pshare <-- API Wrappers (tweepy, facepy) <-- API (Facebook Graph API, Twitter API)

###TODO:

    1. Describe the overall goal of pshare -- why use it?
    2. What are the use cases of pshare?
        - post link / description to facebook (possibly img files)
        - post link / description to twitter (possibly img files)
    3. How are we going to implement above use cases? -- tweepy + facepy + some custom functionality
    4. Design the specifics of the application: possible classes, modules (argparse), examples of usage, dependencies, etc..
    5. Create two different install / build routes:
        - git clone https://github.com/mgzwarrior/pshare.git
        - pip install pshare
