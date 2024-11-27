# Find a Film - A CS50x Project
#### Video Demo:  <https://youtu.be/MP5Dhej5Fic>
#### Description:
This web application helps users find a film that meets a certain search criteria. I was motivated to create this because I often find myself asking, "What film should I watch tonight?"
It queries an IMDB database with more than 400,000 movies. Search results are limited to 50 entries.

An AWS subscription request was made to use IMDb's API to get movie information as it made available, but this request was declined (no reason was given).

Users can limit the search results by entering any (or none) of the following:
-actor
-director
-rating
-release year

The application consist of the following files that will be explained in detail in a different section of this README.md
-app.py
-movies.db
-requirements.txt
-styles.css
-year_dropdown.js
-index.html
-layout.html
-search_results.html


### app.py
This file contains the python code that invokes a flask web application as well as an SQLAlchemy database. It also contains the logic that handles HTTP GET/REQUEST methods and uses conditional logic to make a distinction between the two.

### movies.db
This file is a database that contains information about movies, their ratings, the actors that star in them, the directors that directed them, and tables that map this information together.
A subscription request was made to IMDb's API, but it was declined. As a result, this database is queried instead of using the API to query the latest movie information/data.

### requirements.txt
This file defines the necessary prerequisites for running this web application. Without them, this web application will either fail to work or fail to compile.

### style.css
This file uses CSS (cascading style sheet) to specify the style of HTML content will appear.

### year_dropdown.js
This file contains the javascript code that dynamically populates the dropdown list of release years used as search criteria. This prevents the need to hardcode the "release year" search criteria.

### index.html
This file is the home page that contains the HTML content shown to the end user when they navigate to and use the web application.

### layout.html
This file contains the HTML content that is inherited by every HTML page in this application.

### search_results.html
This file contains the HTML content that displays the search results of user specified criteria.
The results are shown in descending order from highest rated to lowest rated film.

Columns that are shown to the user are:
-Film
-Rating
-Votes
-Released
