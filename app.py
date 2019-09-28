import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import Config
from pymongo import MongoClient
from form import UsernamePasswordConfirm, UsernamePassword
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# connection to mongoDB and set database variable called db
client = MongoClient(Config.MONGO_URI)
print("Mongo is connected!")
db = client.flaskBlog
app.secret_key = os.getenv("SECRET_KEY")

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
@app.route('/login', methods=['GET', 'POST'])
def login():
	"""
	login function that calls on the UserName Password class from form.py,
	then checks to see if the username and password matches those stored
	on the database. If yes, user is logged in. If not, user is redirected
	"""
	#form is linked to the relevant login class
	form = UsernamePassword()
	# if form is validated, continue
	if form.validate_on_submit():
		username_matches = db.users.find_one({'username': request.form['username'].lower()})
		#check to ensure that hashed password matches on entered in form
		if username_matches:
			if check_password_hash(username_matches['password'],request.form['password']):
				session['username'] = request.form['username']
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				flash('Login did not work. Please check username and password')


			
	return render_template('login.html', form=form, title='Login')

# register route for new user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
	"""
	Registration function that calls on the UsernamePasswordConfirm class from form.py,
	then checks to see if the username from form already exists in database. If not, 
	hashes password and adds new user to database.
	"""
	# form is linked to the relevant registration class
	form = UsernamePasswordConfirm()
	# if form is validated, check to find the username in database
	if form.validate_on_submit():
		new_user = db.users.find_one({'username': request.form['username'].lower()})
	# if the username does not exist, the entered password is hashed
		if new_user is None:
		 hash_password = generate_password_hash(request.form['password'])
		 # new username and hashed password are entered into database
		 db.users.insert_one({
                'username': request.form['username'].lower(),
                'password': hash_password,
                })
		 # the username from the form is set to username in current session
		 session['username'] = request.form['username']
		 # current session username is logged in and redirected to home page
		 session['logged_in'] = True
		 flash('Success! Your account has been created!')
		 return redirect(url_for('home'))
		 # if the username already exists, user is redirected to register page
	
	
	return render_template('register.html', form=form, title='Register')

#logout route for users to log out
@app.route('/logout')
def logout():
	"""
	function that logs out users and will redirect to homepage
	"""
	#end the session
	session.clear()
	return redirect(url_for('home'))

						
if __name__ == '__main__':
	app.run(debug=True)  

