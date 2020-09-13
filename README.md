# Pixel Review - Game Review App

The purpose of this application is to allow users to login and write and or edit and delete reviews of the top rated games
for that specific month. 

## UX

The UX for this app uses Bootstrap and Materialize for responsiveness and overall structure of styling. 

### Mongo Database Structure 

The database structure started with 3 collections and ended with a 4th being added for the login systems users

1. [games](https://github.com/OatsRx/Pixel-Review-Project/blob/master/Wireframes/Database%20Structure/games.PNG)

2. [platforms](https://github.com/OatsRx/Pixel-Review-Project/blob/master/Wireframes/Database%20Structure/platforms.PNG)

3. [reviews](https://github.com/OatsRx/Pixel-Review-Project/blob/master/Wireframes/Database%20Structure/reviews.PNG)

4. [users](https://github.com/OatsRx/Pixel-Review-Project/blob/master/Wireframes/Database%20Structure/users.PNG)

### Wireframes

Wireframes can be found in the [rootdirectory/wireframes](https://github.com/OatsRx/Pixel-Review-Project/tree/master/Wireframes/wireframes) of the project

## Features

## Current Features

The frontend features of this application consist of a navigation to login or write a review on the header of
the homepage. Below are a selection of top rated chart games to choose from to write, edit or delete your reviews.
Deleting reviews still needs a confirmation script to avoid accidental deletion of reviews. 
Backend features consist of a basic login system has been started and allows users to login however no implementation
as of yet to end current session. This system uses bcrypt to hash the users password so no plain text is sent to the database.
Post and Get methods are used to send and retrieve data from the html forms to the database.

Demo login: USERNAME: Oats PASSWORD: pass

## Future Features

##### 1. This application needs validation/defensive design applied to the form entry fields in; /register, /login, /write_review and edit_review
#####    this is a high priority for the future of the application.
##### 2. Login sessions made more unique so that users can see each others posts on each review and only be able to edit/delete their own reviews.
##### 3. Login sessions expanded upon to give certain users different permissions to enter different areas of the database.


## Technologies Used

### Languages

##### 1. HTML
##### 2. CSS
##### 3. Javascript
##### 4. Python 3.6

### Frameworks, Libraries and Deployment 

##### 1. Flask 1.1.2
##### 2. Py-Mongo
##### 3. Bootstrap 4.4.1
##### 4. Materialize
##### 5. jQuery 3.4.1
##### 6. MongoDB
##### 7. GitHub
##### 8. Heroku

## Testing

The application has been tested by myself to ensure that the core functions of the app work. These include; writing a review,
editing a review, deleting a review, logging in. There are slight overlaps of buttons on the write/edit task options on some mobile
devices whch needs to be addressed. HTML, CSS and Python code have all been sent through validators.

The main issue which was stated earlier in the features section is the validatin for the backend form data. Although there are some 
validation techniques used in the html forms on the front end to ensure eg. integer is used, implementation of backend python validation
is essential to ensure consistency of data sent to mongo. 

## Deployment

Source code for this application was sent to Github during development and linked to Heroku through a branch that automatically commits
from GitHub. Through development the app was deploying through GitPod on Opera and requires installation of the requirements.txt. 
The config for this application is using an env.py file for the environment variable MONGO_URI in order to link to the database.
To start the application in the GitPod IDE I used during develoment ensure requirements.txt have been installed and run the app.py file
if on local deployment and CTRL+left click IP address in terminal to open project in new window. 

## Credits

##### Content

Text for all existing reviews wask taken from [ign.com](https://www.ign.com/uk)

##### Media 

All pictures were taken from [g2a.com](https://www.g2a.com)

##### Media
Special thanks to: 

Tim from code institute - for providing me with the new course videos before hand
Brian Macharia - for mentoring sessions