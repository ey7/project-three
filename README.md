# Python Flask book blogging app

## Book Blogging App
This Python Flask blogging app allows book lovers to read blogs and article about their favourite authors and books. Users can browse and search all content anonymously, or they can elect to register and sign in, where they can create, update and delete their own content. Full user authentication with hashed passwords gives added security. The app is intended as a resource for book lovers that would grow over time to a treasure trove of information.

 ## UX and Design Planning

Please view the [project strategy document](planning.md) for the app, which details the project strategy, including the project planning of the UX and UI, scope, structure, skeleton and surface. I used [Figma](https://www.figma.com) for the intial website design of the homepage.

- The app will be a fully functional blogging application with full CRUD functionality. All users can read blog content and authorized users can create, update and delete their own content.
- The app will have full user registration, authorization and authentication functionality with hashed passwords.
- Non logged in users will have restricted access to the app, and will only be able to view content.
- Logged in users will also have access to their own content for creating, updating and deleting.
- Registered users will have access to their own acccout page to create, read, update and delete their own blog content.
- Search functionality with a searchbox will be implemented on the blogs page.
- Flashed alert messages for success or warnings to aid and direct the user experience for good UX.
- A delete modal will be implemented on the account page to ensure that registered users do not delete own content by accident. The modal offers a second chance to ensure delete is the intended action.

## User Stories

- As a user, I want to be able to read about the latest book reviews and author news.
- As a user, I want to be able to navigate easily around the site and find the information I need.
- As a user, I want to be able to register easily if I wish.
- As a registered user, I want to be able to create, update and delete my own blog content.
- As a registered user, I want proper security with hashed passwords.
- As a registered user, I want a good user experience with success and warning message alerts, when I login, logout, or engage in CRUD actions on my own content.

## App Content

The app consists of over 10 pages relating to app functionality, such as home, account, blog, blogs, editBlog, addBlog, login, register, search and custom error pages.

## App Style

- A primary colour of green with a secondary colour of orange throughout for visual consistency. 
- A modern sans serif font of Exo 2.
- An off white background with dark grey text for optimum readability.

## Features

- Full CRUD functionality. All users can read content. Authorized users can create, update and delete content.
- Full user registration, authentication, login and logout functionality with hashed passwords courtesy of Werkzeug security. New users can register and existing users can login.
- Individual user account pages that lists a user's authored content, if any.
- Flash message alerts for both success and danger that aid the user experience, in particular with user authentication and CRUD actions.
- Pop out delete modal on the account page that asks the user if they are sure about a delete which cannot be undone.
- Responsive navigation with hamburger drop down menu icon for small and medium screens.
- Search functionality for word search in blog titles.

## Features to be implemented

- Full text search functionality. I would like for the user to be abe to do a full text search.
- I would like to implement a loading spinner that activates when a page is loading.
- Pagination on the blogs and acccout page, to limit the number of blogs on each page.
- Images. It would be nice for the user to have the option to upload a photo with their blog.
- I would like to add a background image or gif animation for the search and error pages.
- I would like to add a forgot password feature whereby the user could reset their password.

## Technologies Used

- HTMl and CSS for website layout and design.
- [Bootstrap](https://getbootstrap.com/) for modern styling with responsive navigation, tables and buttons. 
- Javascript for site functionality.
- [Jquery](https://jquery.com/) and [Popper Js](https://popper.js.org/) for Bootstrap functionality.
- [Google fonts](https://fonts.google.com/) for fast loading on Exo 2 font.
- Git for version control and [Github](https://github.com/) for repository hosting.
-[Heroku](https://heroku.com/) to host the site.
- [Figma](https://www.figma.com) for mock ups of the site.
- [MongoDB](https://www.mongodb.com) for NoSql database functionality.
- [CK Editor](https://www.ckeditor.com) for an attractive editing area on the add and edit blog pages.
  
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
- The app was tested using developer tools throughout the project on multiple browsers - Chrome, Mozilla & Opera etc.
- The developer console was used throughout the project to check for javascript errors and issues.
- The links and buttons on all pages were manually tested to ensure everything was working correctly.
- All breakpoints were tested for different screen sizes and viewports.
- The app was tested on [Responsinator](https://www.responsinator.com/) and [Am I Responsive](http://ami.responsivedesign.is/) to ensure that the site pages were rendering correctly on all types of devices and orientations, such as Ipad and Iphone.
- The app was put through the [HTML5 Validator](https://validator.w3.org/) and some errors and warnings related to stray tags and duplicate ids were fixed.
- The app was put through [CSS Validator](https://jigsaw.w3.org/css-validator/) and some errors were uncovered related to the bootstrap css which is not something that I can control. My own css code was error free.
- I also tested the website on [google mobile friendly](https://search.google.com/test/mobile-friendly) and recieved a mobile friendly result. 
- I tested the website on personal and other family devices such as my laptop and android mobile phone, iPad and iPhone and Samsung Galaxy Tab in both potrait and landscape orientations.

## Issues

## Investigation and resolution of issues

## Image credits

- The favicon for the site was downloaded for free from [iconscout](https://iconscout.com/).
- SVG icons throughout the site were used courtesy of [Zondicons]((https://www.zondicons.com/).

## Acknowledgements

-Thanks to [W3 Schools](https://www.w3schools.com/) and [Flask Documentation](https://flask.palletsprojects.com) who helped with many code ideas and snippets, they have been acknowleged in the code.

- I drew much inspiration and ideas from Brad Traversy, Miguel Grinberg, Corey Schaefer and Pretty Printed, who explained many Flask methods and techniques on Youtube and their personal websites.

## Deployment

### Local Deployment

To deploy locally, firstly you need the following:

- A code editor such as Visual Studio Code, Sublime Text, Atom or another of your choosing.

You must have the the following installed on your machine:

- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [GIT](https://git-scm.com/downloads)

- Also you need to set up an acccount at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for your database.

### Instructions

1. Save a copy of the github repository located at https://github.com/ey7/project-three by clicking the "download zip" button at the top of the page and extracting the zip file to your download folder. If you have Git installed on your machine, you can clone the repository with the following command:

`git clone https://github.com/ey7/project-three`

2. Open a terminal window and change directory (cd) to the the project folder.

3. Create a .flaskenv file which will contain the connection to the database and the secret key for the flask app.

The .env file contents wil look something like the following:
`MONGO_URI='Your Mongo URI connection details'`
`SECRET_KEY='Your secret key'` 

4. Install all required modules with the command: `pip -r requirements.txt`

5. Create a new database on MongoDb  and call it FlaskBlog. In the database, create the following two collections:
USERS
```_id: "automatically generated object ID"
username: "string"
password: "string"```

BLOGS 
```_id: "automatically generated object ID"
image: "string"
posted_on: "integer"
author: "string"
content: "string"```

 6. You can now run the application with the following command: `python app.py`




