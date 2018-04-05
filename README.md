# Flask Mailroom Application

## To Run

All commands to be run from inside the repository directory.
```
$ pip install -r requirements.txt
$ python setup.py
$ python main.py
```

## To Publish to Heroku

All commands to be run from inside the repository directory.
```
$ git init                # Only necessary if this is not already a git repository
$ heroku create
$ git push heroku master  # If you have any changes or files to add, commit them before you push. 
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku run python setup.py
$ heroku open
```
