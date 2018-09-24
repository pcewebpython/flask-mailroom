# Flask Mailroom Application

Running at [http://afternoon-reef-51666.herokuapp.com/donations/](http://afternoon-reef-51666.herokuapp.com/donations/).

## Your Task

Your task is to:

1. Add a page with a form for CREATING new donations from existing donors in the database:
  * The page should have a form, with a field for the donor name and a field for the amount of the donation.
  * The method of the form should be POST.
  * You will need to create a template for this page, inside of the `templates` directory. The template should inherit from `base.jinja2`.
  * You should create a route and a handler function inside of `main.py`. The handler function should accept both GET requests and POST requests.
    * If the handler receives a GET request, then it should render the template for the donation creation page.
    * If the handler receives a POST request (a form submission), then it should attempt to retrieve the name of the donor and the amount of the donation from the form submission. It should retrieve the donor from the database with the indicated name, and create a new donation with the indicated donor and donation amount. Then it should redirect the visitor to the home page.

2. Add navigation elements in `base.jinja2` to the top of both pages. The navigation elements should include links to both the home page and your new donation-creation page.

3. Publish your work to Heroku. If you publish your work to Heroku and then make changes to your application, you will need to publish those changes by commiting your work to your git repository and then executing `git push heroku master`. Make sure that you also `git push origin master` to push your changes to GitHub.

4. Edit the top of this README file, replacing _my_ Heroku link ([http://afternoon-reef-51666.herokuapp.com/donations/](http://afternoon-reef-51666.herokuapp.com/donations/)) with your own Heroku link. If you're unable to get your application running on Heroku, that's no problem. Instead, just write a couple of sentences about where you got hung up.


## Getting Started

I recommend that you begin by forking this repository into your own account, then cloning it to your computer. Then follow the instructions below to run the program. Once you can see the homepage, including a list of donations by Alice, Bob, and Charlie, then you are ready to make your modifications to the program.

## To Run

All commands to be run from inside the repository directory.
```
$ mkvirtualenv flask-mailroom
$ pip install -r requirements.txt
$ python setup.py
$ python main.py
```

Confirm that the application is running on port 6738, and then open your browser to [http://localhost:6738](http://localhost:6738)

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

## Taking it Further

Here are some *optional* ways that you can extend your application:

1. Think about what can go wrong with form submission. What would you like to do if a user enters a name that _does not exist_ in the database of donors? One possibility would be to re-display the donation creation form and inject a message describing the error. Another possibility would be to _create_ a new donor with the given name, along with the indicated donation. Implement either solution.

2. Allow all visitors to view the page of donations, but require that users _login_ in order to enter a donation. This would involve new pages, new models, changes to the database `setup.py` file, and the use of a secret key to encode values into the session.

3. Create a page that allows visitors to view all donations from a single donor. You could accomplish this by creating a new page with a form that allows visitors to submit the name of the donor that they would like to see donations for. If the form has been submitted, then the handler function would retrieve that name, find the indicated donor, retrieve all of their donations, and then inject them into the page to be rendered. Ideally, the method of the form would be GET. This extension would include some steps or combinations of code that I may not have demonstrated in the lesson, but that you could probably puzzle out.

If you choose to perform any of these *optional* extensions, then let us know as a comment to your submission!
