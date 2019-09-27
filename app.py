import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import Config
from pymongo import MongoClient
from form import UsernamePasswordConfirm
app = Flask(__name__)

# connection to mongoDB and set database variable called db
client = MongoClient(Config.MONGO_URI)
print("Mongo is connected!")
db = client.flaskBlog

#home route
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

#experimental users route
@app.route("/users/")
def users():
	user = db.blogs.find_one({"_id": ObjectId('5d8a95cf1c9d440000ed6705')})
	return render_template('users.html', user=user) 

# login route for user login
@app.route('/login')
def login():
	return render_template('login.html')

# register route for new user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
	"""
	Registration function that calls on the UsernamePasswordConfirm class from form.py,
	then checks to see if the username from form already exists in database. If not, 
	hashes password and adds new user to database.
	"""
	# form is linked to the relevant registration class
	form = UsernamePasswordConfirm
	# if form is validated, check to find the username in database
	if form.validate_on_submit():
		new_user = db.users.find_one({'username': request.form['username'].lower()})
	# if the username does not exist, the entered password is hashed	
	if new_user is None:
		 hash_pass = generate_password_hash(request.form['password'])
		 # new username and hashed password are entered into database
		 db.users.insert_one({
                'username': request.form['username'].lower(),
                'pass': hash_pass,
                })
		 # the username from the form is set to username in current session
		 session['username'] = request.form['username']
		 # current session username is logged in and redirected to home page
		 session['logged_in'] = True
		 flash('Success! Your account has been created!')
		 return redirect(url_for('home'))
		 # if the username already exists, user is redirected to register page
	flash('Sorry, username already exists. Please try another')
	return redirect(url_for('register'))

	return render_template('register.html', form=form, title='Register')
						

						
if __name__ == '__main__':
	app.run(debug=True)  

