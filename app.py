import os, math
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from config import Config
from pymongo import MongoClient
from form import UsernamePasswordConfirm, UsernamePassword, ContentTitleForm
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)

# connection to mongoDB and set database variable called db
client = MongoClient(Config.MONGO_URI)
print("Mongo is connected!")
db = client.flaskBlog
app.secret_key = os.getenv("SECRET_KEY")

# ------------HOME ROUTE -------------#

#home route
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


# ------------USER LOGIN, REGISTRATION, AND LOGOUT -------------#

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
		#check to ensure that hashed password matches one entered in form
		if username_matches:
			if check_password_hash(username_matches['password'],request.form['password']):
				session['username'] = request.form['username']
				session['logged_in'] = True
				flash('You are now logged in')
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
		else:
			flash('That username is already taken. Please enter a different username')

	return render_template('register.html', form=form, title='Register')

# User logged in authorization function
# Code credit: https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
def authorized(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You must be logged in to view this page, please login first')
            return redirect(url_for('login'))
    return wrap

#logout route for users to log out
@app.route('/logout')
@authorized
def logout():
	"""
	function that logs user out and will redirect to homepage
	"""
	#end the session
	session.clear()
	flash('You are now logged out')
	return redirect(url_for('home'))


# ------------CREATE, READ, UPDATE AND DELETE FUNCTIONALITY-------------#

# Read all blogs
@app.route('/blogs')
def blogs():

    """
    Displays all blogs. Pagination limits 8 per page.
    """

    blog_limit = 8
    current_page = int(request.args.get('current_page', 1))
    total = db.blogs.count()
    pages = range(1, int(math.ceil(total / blog_limit)) + 1)
    blogs = db.blogs.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*blog_limit).limit(blog_limit)

    return render_template('blogs.html', blogs=blogs, title='Blogs',
    	current_page=current_page, pages=pages)


						
if __name__ == '__main__':
	app.run(debug=True)  

