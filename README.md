# Final Project: HoodHassles

Web Programming with Python and JavaScript


## Getting Started
This is a Forum based website where users can see and post their daily hassles in their neighborhood. When you visit the website it asks you for your location and then it will display the complaints near you. Here the forum is divided into 4 based on the level of complaints: 

1. **Society level complaints** 
- has a range of 0.5km, so all complaints in a 500m radius will be displayed to you which are of society level.
2. **Neighborhood level complaints**
- has a range of 1.5km
3. **Locality level complaints**
- has a range of 4km
4. **City level complaints**
- has a range of 25km 



Note: let's say you visit city forum, then it shows all the complaints in 25kms radius which are of city level, not any other types of complaint like society, etc. 

The main idea is people can see the local problems, upvote it if they feel the same and can gather the appropriate authority's attention to this. Example if you have a water problem in your society then members can post here and get the society's manager attention to this.


## Technical working/logic:
We ask the user for their location in form of latitudes and longitudes. With that when they visit the forum, we calculate the distance between the geo-coordinates of the complaints (in our database) and user's location. 

If the distance is less than the range of the selected forum and the type of complaint is correct then that complaint will be displayed.

## Distinctiveness requirements
- this is a forum-based website, thus distinct from project pizza, 
- also I only had to Project wiki from 2020 course, rest were done in the previous year thus not taken from Project 2 and 4 of 2020.
- also this is not a social network or an e-commerce site. 

## Complexity requirements
- I have used 1 Django model in the database. (min was one) 
- Also used fetch (ajax) to upvote, delete and solve complaints.
- HTML: has 4 pages, which have modal forms controlled by js
- can store images uploaded by the user in the server. (not done in any other project)
- Validation of all the forms in Js (using regex) which will show the error on the form itself.
- used animation for all the pages on the site.
- made custom logos, footer which are mobile responsive
- made the website mobile responsive (@media queries for all pages).
- used Django sessions


# Files

The project name is hoodhassles and it has a Django app in it called hood. 

## /templates: 
1. layout.html
    - has the 2 navigation bars
        - link to change location, forum's link, my complaint's link, new complaint's link, login/logout and user greeting. Its has also a toggle button for smaller screens.
    - has the following modal forms:
        - register, login and new complaint form
    - has the footer
2. city.html
    - it extends layout.html
    - this is page is dynamic, will change the forum's background based on the part of the forum, this same page also works to display "my complaints".
    - displays the complaints in card list form which has no of upvotes, upvote button, title, username, date time, image etc
    - also has JavaScript in middle, where upvote, solve and delete is handled using ajax(fetch).
3. home.html
    - this is the starting point of the website, 
    - here each user has to enter the location to visit the main website
    - to get the location we have a simple form which collects latitude and longitude from the user. 
    - if a new user tries to visit any other page they will be redirected here.
4. error.html
    - a page where some of the errors are displayed
    - has a link to go back to the website

## /static:
1. index.js
    - has functions to enable and disable scroll, when a modal form is clicked
    - has validation functions which are called when a form field is being filled(keypress), also they return false if the form is not valid which will prevent the form from being submitted. This is done for: login, register and new complaint form
        - functions include: disableScroll, enableScroll, checkempty, checklogin, checkpass, checkpassmatch, checkemail, checkreg, checkclick
    - has functions/onclicks that control the opening and closing of the modal forms
2. style.css
    - has styling for all
        - body, navbars, footer, posts, etc.
    - has animations (keyframes)
    - has media queries that make the website mobile responsive
3. home.css
    - animation and other styling for home.html
4. error.css
    - styling for error.html
5. others:
    -  images for background, forum pages, logos, etc.

## /media
- folder where the images uploaded by users for new complaints are stored. 

## Django/python files in hood app
1. views.py in app:
    - has distance function to calculate the distance between two geo-coordinates   
    - has a home function which when the request method is post stores the lati and longi in session, else renders the home page
    - has forum function which gets the complaints from the database, calculates the distance and render the selected page.
    - has a login, logout and register function
    - has new complaint function which adds a new complaint to the db, also stores the image in the database.
    - has functions for an upvote, marking a problem as solved and deleting a problem which returns a JSON.
2. urls.py
    - basic url handling
3. admin.py
    - enables models to be handled in /admin 
    - also a class to manage voters using filter_horizontal
4. model.py
    - has the complaint model 

## Django/python files in the project
1. setting.py
    - added media_root and media URL to store uploaded image in the database
2. urls.py
    - included app's URL file to the project's URL file
    - also added media root for storing images in the database/server.

These were the brief description of the files used in this project. 

# running the application
    - just run the server using 'python manage.py runserver'
    - the visit localhost/hood and you will be greeted with the home page.
    - add your location and there you can see the forum (by default its city)
    - top navbar
        - Click the logo to change the location
        - forum to visit the forum part
        - my complaints to see complaints that you have posted
        - new complaints: opens a form to make a new complaint
        - login/logout
    - lower navbar
        - level of the complaints you want to see in the forum.
    - main body: 
        - list of complaints near you in cards.
    - see the demonstration link attached below for more detailed explanation

## additional information the cs50 staff should know
    - Hello!, I just wanted to tell you that the way I am collecting the location is not ideal but I tried the built-in geolocation in js (had low accuracy) and I also tried Google's API (geocode maps API) but I had a billing account issue. So, that's the reason why I am collecting the information this way. 
     

### Demonstation link: [Video link](https://youtu.be/juu1o7Q-ClA)

### **Licensing: &copy; Tanish Surana**