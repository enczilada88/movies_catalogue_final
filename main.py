#main.py
import tmdb_client
from flask import Flask, render_template, request
from flask import url_for, request
import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    list_types = tmdb_client.get_list_types()
    if selected_list not in list_types:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many = 12, list_type = selected_list)
    return render_template("homepage.html", movies = movies, current_list = selected_list, list_types = list_types)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie = details, cast = cast)



@app.route('/search')
def search():
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)




@app.route('/today')
def today():
    movies = tmdb_client.get_airing_today()
    today = datetime.date.today()
    return render_template("today.html", movies=movies, today=today)

FAVORITES = set()
from flask import url_for, request





FAVORITES = set()

@app.route("/favorites")
def show_favorites():
    if FAVORITES:
        movies = []
        for movie_id in FAVORITES:
            movie_details = tmdb_client.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template("homepage.html", movies=movies)

@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id and movie_title:
        FAVORITES.add(movie_id)
        flash(f'Dodano film {movie_title} do ulubionych!')
    return redirect(url_for('homepage'))

app.secret_key = None
