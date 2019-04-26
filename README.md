# Project Title

SI507_Final_Project
[Link to this repository](https://github.com/Congpeng1125/SI507_Final_Project)
---
## Project Description
My project is a Flask app in which users can see movies stored in the database and source movie using specific input. Users can also have interactions with app and see recommendation of movies from the app.

## How to run
1.  First, you should install all requirements with `pip install -r requirements.txt`
2.  Second, you should run `python SI507_final_project.py`

## How to use
1. Open `http://localhost:5000/` to see the app
2. Enter different commend/input to interact with the app( see the routes )

## Routes in this application
-  `/` -> this is the home page
- `/new/<titlename>/<typename>/<directorname>/<ratingname>/ ` -> this route helps to add a new movie
-  `/total_number` -> this route shows the total number of movies
-  `/recommend` -> this route randomly select movies to users

## How to run tests
run SI507project_tests.py to test code in the main python document

## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
-  [x] This is a completed requirement.
-  [ ] This is an incomplete requirement.

### General
-  [x] Project is submitted as a Github repository
-  [x] Project includes a working Flask application that runs locally on a computer
-  [x] Project includes at least 1 test suite file with reasonable tests in it.
-  [x] Includes a `requirements.txt` file containing all required modules to run program
-  [x] Includes a clear and readable README.md that follows this template
-  [x] Includes a sample .sqlite/.db file
-  [x] Includes a diagram of your database schema
-  [x] Includes EVERY file needed in order to run the project
-  [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
-  [x] Includes at least 3 different routes
-  [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
-  [x] Interactions with a database that has at least 2 tables
-  [x] At least 1 relationship between 2 tables in database
-  [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
-  [ ] Use of a new module
-  [ ] Use of a second new module
-  [x] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
-  [x] A many-to-many relationship in your database structure
-  [ ] At least one form in your Flask application
-  [x] Templating in your Flask application
-  [x] Inclusion of JavaScript files in the application
-  [ ] Links in the views of Flask application page/s
-  [x] Relevant use of `itertools` and/or `collections`
-  [ ] Sourcing of data using web scraping
-  [ ] Sourcing of data using web REST API requests
-  [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
-  [ ] Caching of data you continually retrieve from the internet in some way

### Submission
-  [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
-  [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
