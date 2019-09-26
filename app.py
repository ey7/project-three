import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import Config
from pymongo import MongoClient

app = Flask(__name__)


# connection to mongoDB and set database
client = MongoClient(Config.MONGO_URI)
print("Mongo is connected!")
db = client.flaskBlog


@app.route('/')
def home():
	return render_template('home.html')

@app.route("/users/")
def user_profile():
	user = db.blogs.find_one({"_id": ObjectId('5d8a95cf1c9d440000ed6705')})
	return render_template('users.html', user=user)    

@app.route('/login')
def login():
	return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True)  

