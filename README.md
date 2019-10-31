# Book Klub - A Python Flask book lovers app

## A Flask app for bookworms
This Python Flask app allows book lovers to read reviews and content about their favourite authors and books. Users can browse and search all content anonymously, or they can elect to register and sign in, where they can create, read, update and delete (CRUD) their own content. Full user authentication with hashed passwords gives added security. The app is intended as a resource for book lovers that would grow over time to a treasure trove of information. <hr>
<img src="static/images/bookKlub.jpg" alt="responsive design viewports" style="max-width:100%;">

# Table of Contents

- [UX and Design Planning](#ux-and-design-planning)
- [Wireframes](#wireframes)
- [Project Design Summary](#project-design-summary)
- [User Stories](#user-stories)
- [App Content](#app-content)
- [App Style](#app-style)
- [Features](#features)
   	- [Navbar](#navbar)
	- [Register](#register)
	- [Login](#login)
	- [Logout](#logout)
	- [View all reviews](#view-all-reviews)
	- [View a single review](#view-a-single-recipe)
	- [Search for reviews](#search-for-reviews)
	- [Account](#account)
	- [Create a review](#create-a-review)
	- [Update a review](#update-a-review)
	- [Delete a review](#delete-a-review)
	- [Flash alerts](#flash-alerts)
- [Features to be implemented](#features-to-be-implemented)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
- [Testing](#testing)
- [Further testing](#further-testing)
- [Bugs and known issues](#bugs-and-known-issues)
- [Content credits](#content-credits)
- [Acknowledgements](#acknowledgements)
- [Deployment](#deployment)
	- [Local Deployment](#local-deployment)
	- [Remote Deployment](#remote-deployment)

 ## UX and Design Planning

Please view the [project strategy document](planning.md) for the app, which details the project strategy, including the project planning of the UX and UI, scope, structure, skeleton and surface. 

### Wireframes

The wireframes for the project, created with [Balsamiq](https://balsamiq.com/), can be found [here](https://github.com/ey7/project-three/tree/master/wireframes)

### Project Design Summary

- The app will be a fully functional blogging application with full CRUD functionality. All users can read blog content and authorized users can create, update and delete their own content.
- The app will have full user registration, authorization and authentication functionality with hashed passwords.
- Non logged in users will have restricted access to the app, and will only be able to view content.
- Logged in users will also have access to their own content for creating, updating and deleting.
- Registered users will have access to their own acccout page to create, read, update and delete their own blog content.
- Search functionality with a searchbox will be implemented on the reviews page.
- Flashed alert messages for success or warnings to aid and direct the user experience for good UX.
- A delete modal will be implemented on the account page to ensure that registered users do not delete own content by accident. The modal offers a second chance to ensure delete is the intended action.
- Pagination will be implemented on the book review page and search pages to limit the number of visible entries.

## User Stories

- As a user, I want to be able to read about the latest book reviews and author news.
- As a user, I want to be able to navigate easily around the site and find the information I need.
- As a user, I want to be able to register easily if I wish.
- As a registered user, I want to be able to create, update and delete my own blog content.
- As a registered user, I want proper security with hashed passwords.
- As a registered user, I want a good user experience with success and warning message alerts, when I login, logout, or engage in CRUD actions on my own content.

## App Content

The app consists of over 10 pages relating to app functionality, such as home, account, review, reviews, edit review, add review, login, register, search and custom error pages.

## App Style

- A primary colour of green with secondary colours of orange and grey throughout for visual consistency.
- A modern sans serif font of Exo 2.
- An off white background with dark grey text for optimum readability.
- To improve the UX, I used SVG icons throughout the site. In my opinion, SVG icons look crisper and are easier to work with than font icons. When placed inline they are easier to style, and they also load on the page much faster than font icons. 

## Features

#### Navbar

The navbar is displayed on all pages. When logged out, it displays links to home, reviews, register and login. <hr>
<img src="static/images/loggedOut.png" alt="logged out navbar" style="max-width:100%;">
When logged in, it displays links to home, reviews, account and logout. <hr>
<img src="static/images/loggedIn.png" alt="logged in navbar" style="max-width:100%;">
#### Register

A user can register an account by creating a username and a password. The username must be unique and be between 4 and 20 characters long. If the username is already taken, the username will get a flash message to say that the username is taken. If any field is empty or does not meet the character length or password match requirements, the user will be given an error message. Otherwise if successful the user will be logged in and taken to the home page.<hr>
<img src="static/images/register.png" alt="register page" style="max-width:100%;"> 

#### Login

A user can log in to their account by entering their username and password. Due to the way the app was designed with usernames stored in lower case in the database, usernames must be entered in lowercase. If the password or username is not correct, a warning flash will appear. If the correct details are entered, a new user session will be opened and redirected to the home page.<hr>
<img src="static/images/login.png" alt="login page" style="max-width:100%;">

#### Logout

Logged in users can log out by clicking on the logout link in the navbar. A success flash will tell them that they are logged out and they will be redirected to the home page.

#### View all reviews

The reviews link on the navbar is always visible, regardless of whether the user is logged in or out. It leads to the reviews page which lists all content using bootstrap pagination to limit the number of entries on the page to five titles. Users can scroll to other pages using the pagination buttons to view more content. Content is displayed in decending order, with the newest title entries appearing on the first page.<hr>
<img src="static/images/allreviews.png" alt="all reviews page" style="max-width:100%;">

#### View a single review

When a user clicks on a title to read it, the user is taken to the single review page where all the blog/review content is visible on the page. A small thumbnail image associated with the blog appears in the top left hand corner on desktop and at the top of the screen on mobile and smaller devices.<hr>
<img src="static/images/singlereview.png" alt="single review page" style="max-width:100%;">

#### Search for reviews

On the reviews page, a searchbar appears at the top of the page where a user can search by keyword. They are then redirected to the search page where the results, if any, are displayed. Pagination is also implemented on the page in the case of multiple results.<hr>
<img src="static/images/search.png" alt="search box page" style="max-width:100%;">

#### Account

Logged in users can view their account by clicking on the link in the navbar or home page. An add review button at top gives the option to create new content. The account page will list all of their created book reviews, if any. If the user has content, this will be displayed in table format with a column for title name, author and date posted. For each content entry, there is a corresponding edit and delete button where the user has the option to update or delete directly.<hr>
<img src="static/images/account.png" alt="account page" style="max-width:100%;">

#### Create a review

To create a review, the user can click on the add review button at the top of the account page. This will bring them to a page where a form will allow them to enter a title, content and an image url for their post. The image URL is optional. An error message will display if the title or content fields are left empty. If the add review is successful, the user will be redirected to the account page where they can view the new post.<hr>
<img src="static/images/create.png" alt="create a review page" style="max-width:100%;">

#### Update a review

To update a review, the user can click on the edit review button which sits to the right of each corresponding blog entry. This will bring them to a page where a form will allow them to edit the title, content and/or the image url for their post. The image URL is optional. An error message will display if the title or content fields are left empty. If the edit review is successful, the user will be redirected to the account page where they can view the newly edited post.

#### Delete a review

To delete a review, the user can click on the delete review button which sits to the right of each corresponding blog entry. This will activate a popup delete modal that will ask them if they are sure they want to delete. The user has the option to confirm or cancel the delete. If delete is chosen a flash message will tell them that the review has been deleted. The user will be redirected to the account page where the review will no longer be visible. A cancel action just dismisses the modal with no action taken.
<hr>
<img src="static/images/deleteModal.png" alt="delete modal" style="max-width:100%;">

#### Flash alerts

<img src="static/images/errorFlash.png" alt="error flash message" style="max-width:100%;"> <hr>
Flash messaging for success and warnings have been implemented throughout the site to aid the user experience, particularly where the user interacts with a form for user authetication and CRUD actions. For example, green success flash messages tell the user that their actions were successful, while orange warning messages tell them that they were unsuccessful or performing an action that is forbidden.<hr>
<img src="static/images/successFlash.png" alt="success flash message" style="max-width:100%;">

## Features to be implemented

The following features were not implemented due to time constraints:

- Full text search functionality. I would like for the user to be able to do a full text search.
- I would like to implement a loading spinner that activates when a page is loading.
- I would like to add a forgot password feature whereby the user could reset their password.

## Technologies Used

- HTML and CSS for website layout and design.
- [Bootstrap](https://getbootstrap.com/) for modern styling with responsive navigation, tables and buttons. 
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript) for site functionality.
- [Jquery](https://jquery.com/) and [Popper Js](https://popper.js.org/) for Bootstrap functionality.
- [Google fonts](https://fonts.google.com/) for fast loading on Exo 2 font.
- Git for version control and [Github](https://github.com/) for repository hosting.
- [Heroku](https://heroku.com/) to host the site.
- [Balsamiq](https://balsamiq.com/) for mock ups of the site.
- [MongoDB](https://www.mongodb.com) for NoSql database functionality.
- [CK Editor](https://www.ckeditor.com) for an attractive editing area on the add and edit blog pages.
- [Cloudinary](https://cloudinary.com/) for image delivery via their api to the app.
  
## Resources

- [Stackoverflow](https://stackoverflow.com/)
- [MDN Mozilla Docs](https://developer.mozilla.org/en-US/)
- [W3 Schools](https://www.w3schools.com/)
- [CSS Tricks](https://css-tricks.com/)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Python Docs](https://docs.python.org)
- [YouTube](https://www.youtube.com)
- [Responsinator](https://www.responsinator.com/)
- [Am I Responsive](http://ami.responsivedesign.is/)
- Google
  
## Testing

- The Flask debugger was in constant use during development, in particular with the building of the backend functionality, routes and functions. Any errors or exceptions were investigated.
- All possible users actions relating to forms for CRUD and user authentication were tested on the forms of each and every page, to ensure that the app was stable and did not crash.
- The 404 page was tested to ensure it displayed correctly if an errant url was entered.
- Similarly all navigation links, back and forward buttons and submit and routing buttons were tested to ensure that everything was working as intended.
- All user CRUD functionality and authetication was tested to ensure that all the required queries and actions were being perfomed on the database correctly.

### Testing the authorization function

Only logged in users have access to certain pages. Logged out users should not have access to routes such as accounts and logout. I tested all these and the flash warning message appeared, warning the user that accesss was forbidden.

### User Registration 

I created my own account and made test reviews. I can log in, update my password, add, edit, and delete my own reviews. I also made test accounts to see if it was possible to delete or edit another user's reviews from another account.

### Add A Review

I made test reviews to test the create review function. I tested submitting a review with no image to see if the placeholder image would appear, and it does. I attempted to submit the form without some required fields, but it wasn't possible.

### Update A Review 

I tested a number of reviews to make sure the edit review function was working correctly. When the form is successfully validated, the review updates with the new data.

### Delete A Review 

I tested the delete function on test reviews, and it removes the selected reviews from the database. The modal popped up and worked as intended, deleting the item from the database.

### Read A Single Review

Reviews were tested by clicking on the review cards on the home page. The review data successfully displayed on screen.

### Account Page 

The account page successfully shows user reviews. I made a test account with no reviews to test the view of a new user compared to a user who had content. A new user is told they have no content and is invited to add a  review.

### Further testing

- The app was tested using developer tools throughout the project on multiple browsers - Chrome, Mozilla & Opera etc.
- The developer console was used throughout the project to check for javascript errors and issues.
- The links and buttons on all pages were manually tested to ensure everything was working correctly.
- All breakpoints were tested for different screen sizes and viewports.
- The app was tested on [Responsinator](https://www.responsinator.com/) and [Am I Responsive](http://ami.responsivedesign.is/) to ensure that the site pages were rendering correctly on all types of devices and orientations, such as Ipad and Iphone.
- The app was put through the [HTML5 Validator](https://validator.w3.org/) and some errors and warnings related to stray tags and duplicate ids were fixed.
- The app was put through [CSS Validator](https://jigsaw.w3.org/css-validator/) and some errors were uncovered related to the bootstrap css which is not something that I can control. My own css code was error free.
- I also tested the website on [google mobile friendly](https://search.google.com/test/mobile-friendly) and recieved a mobile friendly result. 
- I tested the website on personal and other family devices such as my laptop and android mobile phone, iPad and iPhone and Samsung Galaxy Tab in both potrait and landscape orientations.

## Bugs and known issues

- If a registered user logged in using an uppercase letter in the name, for example `Eoin instead of eoin`, they would be logged in but treated by the system as a different user. I checked the login code and realised that the `lower()` function was causing this issue. I removed this and the bug was resolved.

- Due to the way the code is set up, a registered user can now only login using lowercase letters. This is a quick fix due to time constraints, but would have to be improved for user authentication on a commercial production app.

- I intially used the standard CK editor for the add and edit review screens, but then realized that the standard toolbar allows the user to upload content such as images that will not render correctly in the app. For this reason, I changed changed it to the basic toolbar which restricts users to a much smaller amount of options such as bold and italic text etc.

## Content credits

- The favicon for the site was downloaded for free from [iconscout](https://iconscout.com/).
- SVG icons throughout the site were used courtesy of [Zondicons](https://www.zondicons.com/).
- Card images and thumbnails were taken from [QBD Bookstore](https://www.qbd.com.au/)
- Book review content was taken from [The Guardian](https://www.theguardian.com/)
- Placeholder image taken from [Texas Teen Reads](https://www.tsl.texas.gov/sites/default/files/public/tslac/ld/projects/ttr/2008/clipartcolor/images/skydiver1_400c.jpg) 
- No copyright infringement is intended as this is an educational project.

## Acknowledgements

- Thanks to [W3 Schools](https://www.w3schools.com/) and [Flask Documentation](https://flask.palletsprojects.com) who helped with many code ideas and snippets, they have been acknowleged in the code.

- I drew much inspiration and code ideas from the following videos and content:

- [Brad Traversy](https://www.youtube.com/watch?v=zRwy8gtgJ1A) 
- [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 
- [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo)
- [Pretty Printed](https://prettyprinted.com/flaskcheatsheet)

## Deployment

### Local Deployment

To deploy locally, firstly you need the following:

- A code editor such as Visual Studio Code, Sublime Text, Atom or another of your choosing.

You must have the the following installed on your machine:

- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [GIT](https://git-scm.com/downloads)

- Also you need to set up an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for your database.

### Instructions

1. Save a copy of the github repository located at https://github.com/ey7/project-three by clicking the "download zip" button at the top of the page and extracting the zip file to your download folder. If you have Git installed on your machine, you can clone the repository with the following command:

`git clone https://github.com/ey7/project-three`

2. Open a terminal window and change directory (cd) to the the project folder.

3. Create a .flaskenv file which will contain the connection to the database and the secret key for the flask app.

The .flaskenv file contents wil look something like the following:
`MONGO_URI='Your Mongo URI connection details'`
`SECRET_KEY='Your secret key'` 

4. Install all required modules with the command: `pip -r requirements.txt`

5. Create a new database on MongoDb and call it flaskBlog. In the database, create the following two collections:
USERS
```
_id: "automatically generated object ID"
username: "string"
password: "string"
```
BLOGS 
```
_id: "automatically generated object ID"
image: "string"
posted_on: "integer"
author: "string"
content: "string"
```

6. You can now run the application with the following command: `python app.py`

7. The website can be visited on localhost, port 5000 at `http://127.0.0.1:5000`

### Remote Deployment

- The app can be deployed to Heroku. Do the following:

1. In the terminal, create a `requirements.txt` file using the command `pip freeze > requirements.txt`

2. In the terminal, create a Procfile by running the `echo web: python app.py > Procfile` command.

3. Push these files along with the project to your GitHub repository.

4. Create a new app on [Heroku dashboard](https://dashboard.heroku.com/apps), give it a name and set the region to whichever is closest to you.

5. From the Heroku dashboard of your app, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the Heroku app to the correct GitHub repository.

7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

Set the following config vars: 

Key | Value 
--- | --- 
IP | 0.0.0.0 |
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
SECRET_KEY | `<your secret key here>`	

8. Click 'Deploy' in the Heroku Dashboard, and select 'enable automatic deployment'.

9. You should now be able to launch the app on Heroku








