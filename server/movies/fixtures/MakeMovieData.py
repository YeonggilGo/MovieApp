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
print(genre_dict)
# cnt = 0
# for i in range(1, 51):
#     movies = requests.get(url.getMovies(i)).json()['results']
#     for temp in movies:
#         Movie.objects.create(
#             title=temp['title'],
#             origin_title=temp['original_title'],
#             poster_path=temp['poster_path'],
#             overview=temp['overview'],
#             backdrop_path=temp['backdrop_path'],
#         )
#         for genre_id in temp['genre_ids']:
#             Movie.objects.get(title=temp['title']).movie_genres.add(genre_dict[gei])
#             genres=[genre_dict[genre_id] for genre_id in temp['genre_ids']],