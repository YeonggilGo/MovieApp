import requests


class URLMaker:
    key = "26098e52c62da6e76a55e7bd6d69635e"

    def __init__(self):
        self.url = ""

    def getMovies(self, i):
        return f'https://api.themoviedb.org/3/movie/popular?api_key={self.key}&language=ko-KR&page={i}'

    def getGenres(self):
        return f'https://api.themoviedb.org/3/genre/movie/list?api_key={self.key}&language=ko-KR'

    def searchMovie(self, word):
        return f'https://api.themoviedb.org/3/search/movie?api_key={self.key}&query={word}&page=1'

    def recommendMovie(self, id):
        return f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key={self.key}&language=ko-KR&page=1'

searchURL = URLMaker()
data = requests.get(searchURL.searchMovie('iron')).json()
print(data['total_results'])
print(data)
for res in data['results']:
    print(res['title'])


# recommendURL = URLMaker()
# re_data = requests.get(recommendURL.recommendMovie(1726)).json()
# print(re_data)
# for re in re_data['results']:
#     print(re['title'])