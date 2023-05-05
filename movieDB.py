import requests

class MovieDB:
    def __init__(self):
        self.apiKey = "ce56ca62b63940274bd48f688a96d270"
        self.baseUrl = "https://api.themoviedb.org/3/"

    def searchMovie(self, query):
        tQuery = query.replace(" ", "+")
        searchUrl = f"{self.baseUrl}search/movie?api_key={self.apiKey}&query={tQuery}"
        response = requests.get(searchUrl).json()
        if not response["results"]:
            return "No Results"
        else:
            movie = response["results"][0]
            return {
                "original_title": movie["original_title"],
                "release_date": movie["release_date"],
                "id": movie["id"],
                "vote_average": movie["vote_average"],
                "overview": movie["overview"]
            }
