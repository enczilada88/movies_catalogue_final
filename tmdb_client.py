import requests


API_TOKEN ="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNjcyZDBkYmU3OGE2NDEzMjY4NTFiMzI2ZWMzOTdiNiIsInN1YiI6IjYwYmZiODlhZWI3OWMyMDA0MGIyYTFmYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.s1y5mhQhzmZbTgGH4avrHba7PnZ6VMs5lUaSPApUeas"


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


# def get_movies_list(list_type):
# return call_tmdb_api(f"movie/{list_type}")

def get_movies_list(list_type):
    return call_tmdb_api(f'movie/{list_type}')


def get_poster_url(poster_path, size="w342"):
    return f'https://image.tmdb.org/t/p/{size}{poster_path}'


def get_movie_info(movie):
    return {"title": movie["title"], "source": movie["poster_path"]}


def get_popular_movies(list_type):
    return call_tmdb_api(f'movie/{list_type}')


def get_movies(how_many, list_type="popular"):
    print("get list: ", list_type)
    data = get_popular_movies(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    return call_tmdb_api(f'movie/{movie_id}')


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_resp = call_tmdb_api(f'movie/{movie_id}/credits')
    return api_resp["cast"]


def get_list_types():
    return ['now_playing', 'popular', 'top_rated', 'upcoming']


def search(search_query):
   base_url = "https://api.themoviedb.org/3/"
   api_token = API_TOKEN
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   endpoint = f"{base_url}search/movie/?query={search_query}"

   response = requests.get(endpoint, headers=headers)
   response = response.json()
   return response['results']



def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    api_token = API_TOKEN
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']

