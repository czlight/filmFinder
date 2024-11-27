from flask import Flask, redirect, render_template, request
from sqlalchemy import create_engine, text



#configure SQLAlchemy engine
engine = create_engine("sqlite+pysqlite:///movies.db", echo=True)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    #handle HTTP POST method
    if request.method == "POST":

        #acquire user inputted data from forms (e.g. actor, director, rating etc.)
        selected_year = request.form.get('yearDropdown')
        actor = request.form.get("actor")
        director = request.form.get("director")

        #replace rating with '0' if no rating is entered by user
        if not request.form.get("rating"):
            rating = 0
        else:
            rating = request.form.get("rating")

        #connect to database engine and run query
        #SQL query was created with assistance from CS50's Duck Debugger at https://cs50.ai/
        with engine.connect() as conn:
            results = conn.execute(text("""SELECT title, ratings.rating, ratings.votes, year, actors.name, direct.name FROM movies JOIN stars ON movies.id = stars.movie_id JOIN directors ON movies.id = directors.movie_id
                                JOIN ratings ON movies.id = ratings.movie_id JOIN people AS actors ON stars.person_id = actors.id JOIN people AS direct ON directors.person_id = direct.id
                                WHERE LOWER(actors.name) LIKE LOWER(:actor)
                                AND year >= :selected_year AND rating >= :rating  AND LOWER(direct.name) LIKE LOWER (:director) ORDER BY ratings.rating DESC
                                LIMIT 50;"""), {"actor": "%" + actor + "%", "selected_year": selected_year, "rating": rating, "director": "%" + director + "%"})

            #get all results from query above
            results = results.fetchall()
        if not results:
           unique_results = False
        else:
            #create empty dictionary to clean up results (i.e. remove duplicate title entries)
            sanitized_results = {}

            for t in results:
                if t[0] not in results:
                    sanitized_results[t[0]] = t

            unique_results = list(sanitized_results.values())

        return render_template("search_results.html", results=unique_results)

    #process HTTP GET request method
    else:
        return render_template('index.html')

@app.route("/search_results")
def search_results():
    return redirect("/",)

if __name__ == '__main__':
    app.run(port=8000)
