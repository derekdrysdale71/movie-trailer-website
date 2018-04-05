import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image = poster_image
        self.trailer_url = trailer_url

    def play_trailer(self):
        webbrowser.open(self.trailer_url)
