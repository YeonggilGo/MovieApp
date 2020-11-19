import json
import requests


class URLMaker:
    key = "26098e52c62da6e76a55e7bd6d69635e"

    def __init__(self):
        self.url = ""

    def getMovies(self, i):
        return f'https://api.themoviedb.org/3/movie/popular?api_key={self.key}&language=ko-KR&page={i}'

    def getGenres(self):
        return f'https://api.themoviedb.org/3/genre/movie/list?api_key={self.key}&language=ko-KR'


url = URLMaker()
genre_url = URLMaker()
genre_list = requests.get(genre_url.getGenres()).json()
genre_dict = {x['id']: x['name'] for x in genre_list['genres']}
data = []
cnt = 0
for i in range(1, 51):
    movies = requests.get(url.getMovies(i)).json()['results']
    for temp in movies:
        cnt += 1
        input_data = {
            "model": "movies.Movie",
            "pk": cnt,
            'fields': {
                'title': temp['title'],
                'origin_title': temp['original_title'],
                'poster_path': temp['poster_path'],
                'genres': [genre_dict[genre_id] for genre_id in temp['genre_ids']],
                'overview': temp['overview'],
                'backdrop_path': temp['backdrop_path'],
            }
        }
        data.append(input_data)
with open("movies.json", "w", -1, "UTF-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False)
