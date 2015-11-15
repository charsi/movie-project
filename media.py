import webbrowser

class Movie():
	"""just a class defining a movie objects"""

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_yt_url, imdb_url, release_year):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster = poster_image_url
		self.trailer = trailer_yt_url
		self.year = release_year
		self.imdb=imdb_url


	def show_trailer(self):
		webbrowser.open(self.trailer)
