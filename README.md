<img src="static/images/website-images/cat-beans-cafe-logo.png" width="200" height="200" alt="Cat Beans Café logo">



# Welcome to Cat Beans Café

## A café website.

> A cat themed, responsive café website with registration and table booking system for customers. Created as a fourth Project Portfolio for Code Institute.

### [Link to the live site](https://cat-beans-cafe-08a84ae29847.herokuapp.com/)

#### - By Karolina Piech

---

## Table of contents 

 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#known-bugs)  
 8. [ Deployment](#deployment)
 9. [ Resources ](#resources)  
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---

# UX

<a name="ux"></a>

## Database planning 

#### Data structure

<img src="static/images/readme-images/lucid-diagram.png" alt="Lucid diagram" width="600">

- After deciding on the kind of the project and features I wanted to implement I used a lucidchart to plan the database structure.
- The above diagram is serving as an initial guide to indicate the types and relationships between data stored.

#### Data models

> UserProfile model

- The revised data models developed as the project evolved into it's current state:

| Key | Name | Field |
|--|--|--|
| PrimaryKey | customer | OnetoOneField  |
| x | first_name | Charfield |
| x | last_name | Charfield |
| x | phone_number | Charfield |
| x | email | Emailfield |

---

> Bookings model

| Key | Name | Field |
|--|--|--|
| ForeignKey | booking_customer | ForeignKey  |
| x | booking_date | DateField |
| x | booking_time | CharField |
| x | tables_booked | CharField |
| x | additional_info  | TextField |
| x | booked_on | DateTimeField |
| x | is_confirmed | IntegerField |
| x | slug | AutoSlugField |

---

## UX design


### Overview

#### Design

> Initial design planning

Early design stage of this project included making png versions of a homepage and login page prototypes.
Thanks to that I could decide on the aesthetic choices before entering the coding stage.

<img src="static/images/readme-images/planning-home.png" alt="Homepage prototype" width="520">
<img src="static/images/readme-images/planning-log-in.png" alt="Login page prototype" width="520">

I wanted the website to look modern, professional and welcoming. I chose the base colours to be in the shades of brown, black and white, as they may be associated with coffee.

#### Site User

- Someone over 16 years old from the café's area
- A cat loving person looking for the place to relax
- Someone who prefers to arrange their bookings digitally rather than over the phone or in person

#### Goals for the website

- To allow customers to see the menu before visiting the café
- To allow customers to plan their booking in advance
- To safely store the bookings data and make it available for designated staff to approve or decline it in an easy way

### Wireframes

The next stage of UX design planning was creating the basic wireframes using [Figma](https://www.figma.com/).
My intention was to create visually pleasing and easy to navigate website. Below I did not include the base homepage and login page, as I used the initial planning examples from above instead.

> Large to medium screens

![About Us page](static/images/readme-images/wireframe-about.png)

![Our Cats page](static/images/readme-images/wireframe-cats.png)

![Contact Us page](static/images/readme-images/wireframe-contact.png)

![Menu page](static/images/readme-images/wireframe-menu.png)

> Small screens

![Home page](static/images/readme-images/wireframe-home-phone.png)

![Login page](static/images/readme-images/wireframe-login-phone.png)

![About Us page](static/images/readme-images/wireframe-about-phone.png)

![Our Cats page](static/images/readme-images/wireframe-cats-phone.png)

![Contact Us page](static/images/readme-images/wireframe-contact-sm.png)



##### [ Back to Top ](#table-of-contents)

---

# Agile Development

## Overview

I started this project alongside GitHub Projects with intention of planning and tracking the workflow to manage the expected workload. After setting out the epics for my project I broke them down into a set of user stories and smaller tasks, to help me monitor my progress and finish the website in time. Outside of user stories I also included a separate issues for creating each module of this README file, as I simply found it more motivating this way. To see the project's Kanban page please click [here](https://github.com/users/TulaUnogi/projects/3/views/1).

## User Stories

Initial stage of the project included stepping into the shoes of the future User. I thought about the features and functionality I would expect from the first use of the website and based on that I created a set of 12 User Stories. I labelled 10 of them as mandatory, as they provide the core functionality and source of important informations for the User. The remaining 2 Stories are labelled as NINTH- Nice To Have, Not Important, as they provide some improvements, but are not necessary for the User to enjoy the website's base functionality. 

The User Stories include the acceptance criteria and are broken down into smaller, bite- size tasks that I would tick on completion, so I could easily track my progress. During the coding session I would record the encountered bugs, issues and solutions related to the Story in the comments below. Once all of the tasks in the Issue are completed I would move the User Story form "In progress" to "Completed" card im my project's Kanban.

> List of Mandatory User Stories

1. [USER STORY: DEPLOYMENT](https://github.com/TulaUnogi/cat-beans-cafe/issues/16)
2. [USER STORY: ADMIN PANEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/17)
3. [USER STORY: CREATE AN ACCOUNT](https://github.com/TulaUnogi/cat-beans-cafe/issues/18)
4. [USER STORY: EDITING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/22)
5. [USER STORY: DELETING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/23)
6. [USER STORY: TABLE BOOKING](https://github.com/TulaUnogi/cat-beans-cafe/issues/21)
7. [USER STORY: NAVBAR AND FOOTER](https://github.com/TulaUnogi/cat-beans-cafe/issues/20)
8. [USER STORY: ABOUT US](https://github.com/TulaUnogi/cat-beans-cafe/issues/19)
9. [USER STORY: MENU](https://github.com/TulaUnogi/cat-beans-cafe/issues/26)
10. [USER STORY: GOOGLE MAPS](https://github.com/TulaUnogi/cat-beans-cafe/issues/25)

> NINTH: Not Important, Nice To Have

11. [USER STORY: CAT CAROUSEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/24)
12. [USER STORY: BOOKING CANCELLATION](https://github.com/TulaUnogi/cat-beans-cafe/issues/27)

##### [ Back to Top ](#table-of-contents)

---

# Features implemented

- [USER STORY: DEPLOYMENT](https://github.com/TulaUnogi/cat-beans-cafe/issues/16)
- [USER STORY: ADMIN PANEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/17)
- [USER STORY: NAVBAR AND FOOTER](https://github.com/TulaUnogi/cat-beans-cafe/issues/20)
- [USER STORY: ABOUT US](https://github.com/TulaUnogi/cat-beans-cafe/issues/19)
- [USER STORY: MENU](https://github.com/TulaUnogi/cat-beans-cafe/issues/26)
- [USER STORY: GOOGLE MAPS](https://github.com/TulaUnogi/cat-beans-cafe/issues/25)
- [USER STORY: CREATE AN ACCOUNT](https://github.com/TulaUnogi/cat-beans-cafe/issues/18)
- [USER STORY: EDITING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/22)
- [USER STORY: DELETING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/23)
- [USER STORY: TABLE BOOKING](https://github.com/TulaUnogi/cat-beans-cafe/issues/21)
- [USER STORY: CAT CAROUSEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/24)


### Navbar and Footer:

- Navbar and footer are present on every page
- Navbar's content changes depending on user authentication, allowing access to profile and user bookings
- Footer includes café's opening times, social links and address to provide the necessary informations in an easy way.

### Index page:

- The homepage provides the links to booking and about us page.
- It can be accessed without signing in.

### About Us page:

- Main page includes a short information about the café and set of 4 cards with pictures and description.
- Each of the card includes the button, that triggers a fullscreen modal.
- The modals contain informations about the menu, contact details with embedded google maps, link to booking page and gallery with cat pictures (cat carousel).
- About Us page can be accessed without signing in.

### Authentication and profile management:

- User can sign up to create their profile 
- User can log in to their account and update their informations
- User can delete their account alltogether with all their data
- The authentication process is safe thanks to [Django-AllAuth](https://github.com/pennersr/django-allauth) and csrf tokens.

### Bookings:

- User can pass their data to create a booking.
- User can edit their selected booking.
- Currently the initial version of booking cancellation view has not been fully implemented. I decided to implement an automatic delete_booking view, that allows User to quickly remove their booking from the system.

### Responsiveness:

- Website is responsive thanks to Bootstrap and media queries applied.
- There's a hamburger navbar on small devices.

##### [ Back to Top ](#table-of-contents)

---

# Features Left to Implement

- [USER STORY: BOOKING CANCELLATION](https://github.com/TulaUnogi/cat-beans-cafe/issues/27) - As I've mentioned the initial version of this model is left for now since customer can currently fully delete their booking. 

##### [ Back to Top ](#table-of-contents)

---

# Technology used 

- Html - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for timeout in messages
- Django - framework used to build this project
- Jinja - templating language rendering logic within html documents
- Bootstrap 5 - front end framework used by me alongside Django, helps with fast and efficient styling
- Heroku PostgreSQL - used as the database
- Font Awesome - for social media icons
- Google Fonts- currently only for the hero image font
- GitHub - for storing the code and for the projects Kanban
- Heroku - for hosting and deployement of this project
- Cloudinary - hosting the static files 
- Git - version control tool

##### [ Back to Top ](#table-of-contents)

---

# Testing

### Responsiveness

I was testing for responsiveness on an Ideapad laptop and a Samsung Galaxy A5 using the most up to date versions of Google Chrome, Mozilla Firefox and Opera versions. For more detailed testing I was using Google DevTools.

> Index page:

![Index page](static/images/readme-images/responsive-index.png)


> About Us page:

![Index page](static/images/readme-images/responsive-about.png)


> Sign Up page:

![Index page](static/images/readme-images/responsive-signup.png)


> Sign In page:

![Index page](static/images/readme-images/responsive-sign-in.png)



### Manual testing

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create profile | Pass |
| User can log into profile | Pass |
| User can log out of profile | Pass |
| Messages are displaying | Pass |
| Messages are dismissable by button and timeout | Pass |



---

#### User Navigation Tests

| Test | Result  |
|--|--|
| User can easily navigate to Bookings | Pass |
| User can access About Us page| Pass|
| User access their account page|Pass|
| User can access the card content in About Us|Pass|
| SuperUser can access admin page|Pass|



---

#### Account Authorisation Tests

| Test | Result  |
|--|--|
| Only Superuser can access admin page |Pass|
| Non authorised user book a table | Pass |
| Non authorised user won't access profile page| Pass|



---

#### Booking and Profile Tests

| Test |Result  |
|--|--|
|User can make a booking | Pass |
|User can view all of their bookings | Pass |
|User can delete their booking | Pass |
|User can edit booking | Pass |
|User can make more than one booking | Pass |
|User can delete their account | Pass |
|User can edit their information | Pass |
|User can see the confirmation information | Pass |



---

#### Admin Tests

| Test |Result  |
|--|--|
|Items display correctly on front-end when updated / added |Pass|
|Admin can confirm or decline bookings |Pass|


##### [ Back to Top ](#table-of-contents)

---
 
# Known bugs 

- I observed one blue submit button- it is automatically generated by crispy forms and somehow the form settings did not applied to this button. It's a small bug of low priority for me at the current stage.
- There's small image clipping during the cat carousel transitions on smaller screens.
- The function that was supposed to prevent booking dates in the past is currently preventing nothing, unfortunately... You may be brave and try to trick the system into timetravelling, but Admin will always see what day the booking was made on anyway and won't accept such a silly tricks!


##### [ Back to Top ](#table-of-contents)

---

# Deployment

#### The deployment stage of the website should follow the steps below:

> Create the Heroku app

- Sign up / Log in to Heroku
- In Heroku Dashboard page select 'New' and then 'Create New App'
- Name a project - I decided on the Cat Beans Café (the app's name must be unique)
- Select EU as that was my region in the moment of creating the app
- Select "Create App"
- In the "Deploy" tab choose GitHub as the deployment method
- Connect your GitHub account/ find and connect your GitHub repository

> Set up enviroment variables

- In the Django app editor create env.py in the top level
- In env.py import os
- In env.py set up necessary enviroment variables:
  - add a secret key using: os.environ['SECRET_KEY'] = 'your secret key'
  - for the database variable the line should include os.environ['DATABASE_URL']= 'Paste the database link in here'
  - in settings.py replace value of SECRET_KEY variable with os.environ.get('SECRET_KEY')
  - in settings.py change the value of DATABASES variable to 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
- In Django app's settings.py on top of the file add:
```
from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
- Navigate to the "Settings" tab in Heroku.
- Open the "Config Vars" section and add DATABASE_URL as Key and the database link from app's env.py as Value
- Add SECRET_KEY for the Key value and the secret key value from env.py as the Value
- In the terminal migrate the models over to the new database connection
- In settings.py add the STATIC files settings as follows:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
- Change the templates directory in settings.py to: TEMPLARES_DIR = os.path.join(BASE_DIR, 'templates')
- In TEMPLATES variable change the 'DIRS' key to look like this: 'DIRS': [TEMPLARES_DIR],
- Add Heroku to the ALLOWED_HOSTS list (the format will be your-app-name.herokuapp.com, you can copy it from the Domains section in Settings tab in your Heroku app)
- If you haven't done that up to this point, then create in your Django app's code editor new top level folders: static and templates
- Create a new file on the top level directory - Procfile, remembering to use a capital letter
- Within the Procfile add following:
```
web: guincorn PROJECT_NAME.wsgi
``` 
- In the terminal, add the changed files, commit and push to GitHub

> Heroku deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually 
- Heroku will display a build log- watch the build logs for any errors
- Once the build process is completed Heroku displays 'Your App Was Successfully Deployed' message and a link to the app to visit the live site
- As my first 2 build attempts failed I needed to apply changes to my code (I forgot to set up the static files and templates) to successfully deploy on the 3rd time 

#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository. You can do this with following steps:

- Log in to GitHub or create an account
- Enter this [repository link](https://github.com/TulaUnogi/cat-beans-cafe)
- Select "Fork" from the top of the repository
- A copy of the repository should now be created in your own repository

#### Create a clone of this repository

Creating a clone enables you to make a copy of the current version of this repository to run the project locally. To do this follow steps below:

- Navigate to https://github.com/TulaUnogi/cat-beans-cafe
- Click on the <>Code button at the top of the list of files
- Select the "HTTPS" option on the "Local" tab and copy the URL it provides to the clipboard
- Navigate to your code editor and in the terminal change the directory to your chosen location 
- Type "git clone" and paste the GitHub repository's link
- Press enter and git will clone the repository for you

##### [ Back to Top ](#table-of-contents)

---

# Resources

- [Code Institute Full Stack Development course materials](https://codeinstitute.net/global/full-stack-software-development-diploma/?sitelink=FullStackDiploma-IRL&utm_term=code+institute&utm_campaign=CI+-+IRL+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=635725005315&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code+institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAgqGrBhDtARIsAM5s0_l13h8fkiqZeHnw16zshbX6svuL8YJNrw6G-RFdq03RQybQXLSoZiYaAjGqEALw_wcB) 
- [Django documentation](https://www.djangoproject.com/)
- [Crispy forms docs](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Stack overflow](https://stackoverflow.com/)
- [Slack](https://slack.com/intl/en-ie/)

##### [ Back to Top ](#table-of-contents)

---

# Credits and acknowledgements

> Pictures

- [Mid-coated Brown Cat](https://www.pexels.com/photo/mid-coated-brown-cat-982865/) by <b>Alena Koval</b> on Pexels
- [Cat at the table](https://unsplash.com/photos/black-cat-on-white-table-ZxChxgJa6X0) by <b>Madalyn Cox</b> on Unsplash
- [Cup of coffee](https://pixabay.com/photos/tea-cat-coffee-coffee-shop-cup-2343391/) by <b>yukiqwa</b> on Pixabay
- [Black Steel Welcome Hanging Signage](https://www.pexels.com/photo/black-steel-welcome-hanging-signage-1406282/) by <b>Henry & Co.</b> on Pexels
- [Menu background](https://pixabay.com/photos/coffee-mug-heart-caffeine-food-5176961/) by <b>Konrad Janik</b> on Pixabay

- Cat carousel pictures:
  1. [Fluffy black cat](https://pixabay.com/photos/couch-cat-pet-feline-animal-6654015/) by <b>Spike Summers</b> on Pixabay 
  2. [Calico cat](https://www.pexels.com/photo/calico-cat-1359300/) by <b>Cats Coming</b> on Pexels
  3. [Orange tabby cat](https://www.pexels.com/photo/adorable-animal-cat-close-up-208930/) by <b>Pixabay</b> on Pexels
  4. [Cat with a mouse toy](https://www.pexels.com/photo/cat-with-a-mouse-toy-3216568/) by <b>lil artsy</b> on Pexels
  5. [Two cosy tabby cats](https://www.pexels.com/photo/two-tabby-kittens-lying-down-1787414/) by <b>Cats Comin</b> on Pexels
  6. [Little kitten](https://www.pexels.com/photo/close-up-photo-of-orange-tabby-cat-2581153/) by <b>samer daboul</b> on Pexels
  7. [Christmas kitten](https://www.pexels.com/photo/close-up-photography-of-white-cat-besides-christmas-lights-735423/) by <b>Eftodii Aurelia</b> on Pexels

> Code

- <b>[Raymond Penners](https://github.com/pennersr)</b> for amazing Allauth and [Allauth templates](https://github.com/pennersr/django-allauth/tree/main/allauth/templates/account)
- <b>Roger Pfäffli</b>, Code Institute Alumnus for explaining on Slack how to set up development and DEBUG variables in env.py
- <b>[Coding Yaar](https://codingyaar.com/shorts/bootstrap-navbar-toggler-color-change/)</b> for Bootstrap navbar toggler colour change tutorial
- <b>[May.D from Stack Overflow](https://stackoverflow.com/questions/50439356/django-date-validation-help-needed)</b> for date validation
- <b>Tutors Jason and Oisin</b> for pointing me in the good direction and helping with understanding the code parts I've been struggling with
- <b>My mentor Narender Singh</b> for his patience and all the help and support
- <b>[willeM_ Van Onsem](https://stackoverflow.com/questions/77632628/init-got-an-unexpected-keyword-argument-id/77632951#77632951)</b> for helping me with fixing my edit booking class

##### [ Back to Top ](#table-of-contents)
