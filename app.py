import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# environment variables
app.config["MONGO_DBNAME"] = "flaskBlog"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/user/<username>")
def user_profile(username):
    user = mongo.db.blogs.find_one_or_404({"_id": password})
    return render_template("users.html",
        user=user)    

@app.route('/login')
def login():
	return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)  

