import os, math, datetime
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


# ------------USER LOGIN, REGISTRATION, ACCOUNT AND LOGOUT -------------#

# login route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
	"""
	login function that calls on the UserName Password class from form.py,
	then checks to see if the username and password matches those stored
	on the database. If yes, user is logged in. If not, user is redirected
	"""
	if 'logged_in' in session:
		flash ('You are already logged in', 'danger')
		return redirect(url_for('home'))
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
				flash('You are now logged in', 'info')
				return redirect(url_for('home'))
		else: 
			flash('Login did not work. Please check username and password', 'danger')			
			
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
		 flash('Success! Your account has been created!', 'info')
		 return redirect(url_for('home'))
		 # otherwise flash an error message
		else: flash('That username is already taken. Please enter a different username', 'danger')

	return render_template('register.html', form=form, title='Register')

# User logged in authorization function
# Code credit: https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
def authorized(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You must be logged in to acccess this page', 'danger')
            return redirect(url_for('login'))
    return wrap

# user account route and function
@app.route('/account/<account_name>')
@authorized
def account(account_name):
	# if account name is not equal to username in session, deny access
	if account_name != session.get('username'):
		flash('Access denied, you are not the account owner', 'danger')
		return redirect(url_for('home'))
	else:
		# assigns the current user
		current_user = db.users.find_one({'username': account_name })
		# assigns the current_users blogs
		current_user_blogs = db.blogs.find({'author': account_name}).sort([('_id', -1)])
		# get the count of the user's blogs
		count = db.blogs.find({'author': account_name }).count()
		#return the acccount template

	return render_template('account.html', account_name=account_name, current_user=current_user,
		current_user_blogs=current_user_blogs, count=count, title='My Account')

#logout route for users to log out
@app.route('/logout')
@authorized
def logout():
	"""
	function that logs user out and will redirect to homepage
	"""
	#end the session
	session.clear()
	flash('You are now logged out', 'info')
	return redirect(url_for('home'))


# ------------CREATE, READ, UPDATE AND DELETE FUNCTIONALITY-------------#

#CREATE
# Add a blog
@app.route('/add_blog', methods=['GET', 'POST'])
@authorized
def add_blog():
	"""
	add_blog function that calls on the ContentTitleForm class from form.py
	Only authorized users (logged in) can create blogs.
	"""
	# form variable set to ContentTitleForm
	form = ContentTitleForm(request.form)
	# get author details from username in session
	author = session.get('username')
	posted_on = datetime.datetime.now().strftime("%d-%b-%Y")

	if request.method == 'GET':
		# render the template with the form
		return render_template('add_blog.html', form=form, title='Add Blog')

	if request.method == 'POST' and form.validate_on_submit():
		# creates new blog with the data entered in form
		blog = db.blogs.insert_one({
			'title': request.form['title'],
			'content': request.form['content'],
			'author': author,
			'posted_on': posted_on,
			})
		flash('New Blog Added!', 'info')
		return redirect(url_for('account', account_name=author))
	else:
		flash('You cannot have empty edit fields', 'danger')
		return redirect(url_for('account', account_name=author))	

#READ
# Read all blogs
@app.route('/blogs')
def blogs():
    """
    Displays all blogs, starting with the most recent.
    """
    blogs = db.blogs.find().sort('_id', pymongo.DESCENDING)

    return render_template('blogs.html', blogs=blogs, title='Blogs')

# Read and display one blog
@app.route('/blog/<blog_id>')
def blog(blog_id):
	"""
	Display one blog
	"""
	# assign the variable blog to the id of the blog passed in
	blog = db.blogs.find_one({'_id': ObjectId(blog_id)})
	# If logged in, user set to session username, author set to session user id
	if 'logged_in' in session:
		current_user = db.users.find_one({'username': session['username']})
		author = db.users.find_one({'username': session['username']})['_id']

		return render_template('blog.html', blog=blog, title=blog['title'], current_user=current_user, author=author)
	else:
		return render_template('blog.html', blog=blog, title='Blog')

#UPDATE
# Update a particular blog
@app.route('/edit_blog/<blog_id>', methods=['GET', 'POST'])
@authorized
def edit_blog(blog_id):
	"""
	Allows an authorized user to edit his/her own posts only.
	Calls on the ContentTitleForm class from form.py
	"""
	#  assign the current_user
	current_user = session.get('username')
	#  assign the current blog post
	blog_selected = db.blogs.find_one({'_id': ObjectId(blog_id)})
	# assign the posted_on variable
	posted_on = datetime.datetime.now().strftime("%d-%b-%Y")
	# assign the form to the relevant form class from form.py
	form = ContentTitleForm()
	# if the current username does not match that of the blog_selected author, block the edit
	if current_user != blog_selected['author']:
		flash('Sorry only the author can edit this blog', 'danger')
		return redirect (url_for('blog', blog_id=blog_id))
	else:
		# fill the form with the selected data
		form = ContentTitleForm(data=blog_selected)

		# if the method is post and the form validates
		if request.method == 'POST' and form.validate_on_submit():
			
			# blog is updated with the changes entered into form
			blog = db.blogs.update_one({'_id': ObjectId(blog_id)}, {'$set': {
				'title': request.form['title'],
				'content': request.form['content'],
				'author': current_user,
				'posted_on': posted_on,
				}})

			flash('Success! Your blog has been updated!', 'info')
			return redirect (url_for('account', account_name=current_user))
		else:
			flash('Please note that you must fill in both fields', 'danger')
			return render_template('edit_blog.html', blog=blog_selected, form=form, title='Edit Blog')

#DELETE
# Delete a particular blog
@app.route('/delete/<blog_id>', methods=['GET','POST'])
@authorized
def delete(blog_id):
	"""
	function to delete the current user's blogs. 
	Only blog author can delete their own work.
	"""
	# assigns the current user
	current_user = session.get('username')
	# assigns the blog
	blog_selected = db.blogs.find_one({'_id': ObjectId(blog_id)})
	#if the current username does not match that of the blog_selected author, block the delete
	if current_user != blog_selected['author']:
		# user gets a message to say they cannot delete this blog
		flash('You must be the author to delete this blog', 'danger')
		return redirect(url_for('account', account_name=current_user))
	else:
		#blog is deleted
		db.blogs.delete_one({'_id': ObjectId(blog_id)})
		flash('Success, your blog has been deleted', 'info')
		return redirect(url_for('account', account_name=current_user))

#SEARCH
# Allows a user to make a text search
@app.route('/search')
def search():
	"""
	Text search functionality. Blog title is a searchable index.
	In the mongo shell, type: db.blogs.createIndex({title: "text"})
	"""
	# assign the search query variable
	search_query = request.args.get('search_query')
	# assign the page variable
	current_page = int(request.args.get('current_page', 1))
	per_page = 5
	# search results will be sorted by id
	results = db.blogs.find({'$text': {'$search': str(search_query)}},
		{'score': {'$meta': 'textScore'}}).sort('_id', pymongo.ASCENDING).skip((current_page -1 )*per_page).limit(per_page)

	return render_template('search.html',
	current_page=current_page,
	per_page=per_page,
	search_query=search_query,
	results=results,
	title='Search'
	)

# Error pages
# 404 error page
@app.errorhandler(404)
def page_not_found(error):

	return render_template('errors/404.html'), 404

#500 error page
@app.errorhandler(500)
def internal_server_error(error):

	return render_template('errors/500.html'), 500

#403 error page
@app.errorhandler(403)
def access_forbidden(error):

	return render_template('errors/403.html'), 403

						
if __name__ == '__main__':
	app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)  

