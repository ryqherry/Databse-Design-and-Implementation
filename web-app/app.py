#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, make_response
from markupsafe import escape
import pymongo
import datetime
from bson.objectid import ObjectId
import os
import subprocess

# instantiate the app
app = Flask(__name__)

# load credentials and configuration options from .env file
# if you do not yet have a file named .env, make one based on the template in env.example
import credentials
config = credentials.get()

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

# make one persistent connection to the database
connection = pymongo.MongoClient(config['MONGO_HOST'], 27017, 
                                username=config['MONGO_USER'],
                                password=config['MONGO_PASSWORD'],
                                authSource=config['MONGO_DBNAME'])
db = connection[config['MONGO_DBNAME']] # store a reference to the database

# set up the routes

@app.route('/')
def home():
    """
    Route for the home page
    """
    return render_template('index.html')


@app.route('/read')
def read():
    """
    Route for GET requests to the read page.
    Displays some information for the user with links to other pages.
    """
    docs = db.exampleapp.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp
    return render_template('read.html', docs=docs) # render the read template


@app.route('/readByLike')
def readByLike():
    """
    Route for GET requests to the readByLike page.
    Displays some information for the user with links to other pages.
    """
    docs = db.exampleapp.find({}).sort("like", -1) # sort in descending order of likes of posts
    return render_template('readByLike.html', docs=docs) # render the readByLike template


@app.route('/searchUser')
def searchU():
    """
    Route for GET requests to the search page.
    Displays a form users can fill out to search for all posts and comments of a specific user.
    """
    return render_template('searchByUser.html') # render the search template


@app.route('/searchUser', methods=['POST'])
def search_user():
    """
    Route for POST requests to the search page.
    Accepts the form submission data for the specified user and shows all the posts and comments by that user.
    """
    name = request.form['fname']
    docs = db.exampleapp.find({"$or":[{"name": name}, {"commentName": name}]})
    count = db.exampleapp.count_documents({"$or":[{"name": name}, {"commentName": name}]})
    return render_template('readByUser.html', name=name, docs=docs, count=count)

@app.route('/searchCategory')
def searchC():
    """
    Route for GET requests to the search page.
    Displays a form users can fill out to search for all posts and comments of a specific category.
    """
    return render_template('searchByCategory.html') # render the search template


@app.route('/searchCategory', methods=['POST'])
def search_category():
    """
    Route for POST requests to the search page.
    Accepts the form submission data for the specified category.
    """
    category = request.form['fcategory']
    docs = db.exampleapp.find({"category": category})
    count = db.exampleapp.count_documents({"category": category})
    return render_template('readByCategory.html', docs=docs, count=count)

@app.route('/create')
def create():
    """
    Route for GET requests to the create page.
    Displays a form users can fill out to create a new document.
    """
    return render_template('create.html') # render the create template


@app.route('/create', methods=['POST'])
def create_post():
    """
    Route for POST requests to the create page.
    Accepts the form submission data for a new document and saves the document to the database.
    """
    name = request.form['fname']
    category = request.form['fcategory']
    message = request.form['fmessage']
    comment = ''
    commentName = ''
    commented_at = ''
    like = 0
    image = request.form['fimage']

    # create a new document with the data the user entered
    doc = {
        "name": name,
        "category": category,
        "message": message, 
        "created_at": datetime.datetime.utcnow(),
        "comment": comment,
        "commentName": commentName,
        "commented_at": commented_at,
        "like": like,
        "image": image
    }
    db.exampleapp.insert_one(doc) # insert a new document

    return redirect(url_for('read')) # tell the browser to make a request for the /read route


@app.route('/edit/<mongoid>')
def edit(mongoid):
    """
    Route for GET requests to the edit page.
    Displays a form users can fill out to edit an existing record.
    """
    doc = db.exampleapp.find_one({"_id": ObjectId(mongoid)})
    return render_template('edit.html', mongoid=mongoid, doc=doc) # render the edit template


@app.route('/edit/<mongoid>', methods=['POST'])
def edit_post(mongoid):
    """
    Route for POST requests to the edit page.
    Accepts the form submission data for the specified document and updates the document in the database.
    """
    name = request.form['fname']
    category = request.form['fcategory']
    message = request.form['fmessage']
    image = request.form['fimage']

    db.exampleapp.update_one(
        {"_id": ObjectId(mongoid)}, # match criteria
        { "$set": {
            "name": name,
            "category": category,
            "message": message,
            "image" : image,
            "created_at": datetime.datetime.utcnow() }
        }
    )

    return redirect(url_for('read')) # tell the browser to make a request for the /read route


@app.route('/comment/<mongoid>')
def comment(mongoid):
    """
    Route for GET requests to the comment page.
    Displays a form users can fill out to comment an existing record.
    """
    doc = db.exampleapp.find_one({"_id": ObjectId(mongoid)})
    return render_template('comment.html', mongoid=mongoid, doc=doc)


@app.route('/comment/<mongoid>', methods=['POST'])
def comment_post(mongoid):
    """
    Route for POST requests to the comment page.
    Accepts the form submission data for the specified document and updates the document in the database.
    """
    commentName = request.form['fcommentName']
    comment = request.form['fcomment']

    db.exampleapp.update_one(
        {"_id": ObjectId(mongoid)}, # match criteria
        { "$set": {
            "comment": comment,
            "commentName": commentName,
            "commented_at": datetime.datetime.utcnow() }
        }
    )

    return redirect(url_for('read')) # tell the browser to make a request for the /read route


@app.route('/editComment/<mongoid>')
def editComment(mongoid):
    """
    Route for GET requests to the edit comment page.
    Displays a form users can fill out to edit a comment to an existing record.
    """
    doc = db.exampleapp.find_one({"_id": ObjectId(mongoid)})
    return render_template('editComment.html', mongoid=mongoid, doc=doc)


@app.route('/editComment/<mongoid>', methods=['POST'])
def edit_comment(mongoid):
    """
    Route for POST requests to the edit page.
    Accepts the form submission data for the specified document and updates the document in the database.
    """
    commentName = request.form['fcommentName']
    comment = request.form['fcomment']

    db.exampleapp.update_one(
        {"_id": ObjectId(mongoid)}, # match criteria
        { "$set": {
            "comment": comment,
            "commentName": commentName,
            "commented_at": datetime.datetime.utcnow() }
        }
    )

    return redirect(url_for('read'))


@app.route('/deleteComment/<mongoid>')
def deleteComment(mongoid):
    """
    Route for GET requests to the delet comment page.
    Deletes the comment for the specified record from the database, and then redirects the browser to the read page.
    """
    db.exampleapp.update_one(
        {"_id": ObjectId(mongoid)},
        { "$set": {
            "comment": "",
            "commentName": "",
            "commented_at": "" }
        }
    )
    return redirect(url_for('read'))


@app.route('/like/<mongoid>')
def like(mongoid):
    """
    Route for GET requests to the like page.
    Likes the specified record, and then redirects the browser to the read page.
    """
    db.exampleapp.update_one(
        {"_id": ObjectId(mongoid)},
        { "$inc": {
            "like": 1 }
        }
    )

    return redirect(url_for('read'))


@app.route('/delete/<mongoid>')
def delete(mongoid):
    """
    Route for GET requests to the delete page.
    Deletes the specified record from the database, and then redirects the browser to the read page.
    """
    db.exampleapp.delete_one({"_id": ObjectId(mongoid)})
    return redirect(url_for('read')) # tell the web browser to make a request for the /read route.


@app.route('/webhook', methods=['POST'])
def webhook():
    """
    GitHub can be configured such that each time a push is made to a repository, GitHub will make a request to a particular web URL... this is called a webhook.
    This function is set up such that if the /webhook route is requested, Python will execute a git pull command from the command line to update this app's codebase.
    You will need to configure your own repository to have a webhook that requests this route in GitHub's settings.
    Note that this webhook does do any verification that the request is coming from GitHub... this should be added in a production environment.
    """
    # run a git pull command
    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    pull_output = process.communicate()[0]
    # pull_output = str(pull_output).strip() # remove whitespace
    process = subprocess.Popen(["chmod", "a+x", "flask.cgi"], stdout=subprocess.PIPE)
    chmod_output = process.communicate()[0]
    # send a success response
    response = make_response('output: {}'.format(pull_output), 200)
    response.mimetype = "text/plain"
    return response

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    #import logging
    #logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(debug = True)
