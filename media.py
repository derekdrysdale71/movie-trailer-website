import webbrowser


# Store required movie info
class Movie():
    ''' 
    The Movie class represents a movie item on the website

    Attributes:
        title (str): Movie title
        storyline (str): Movie tagline
        poster_img_url (str): URL to the movie poster image
        trailer_youtube_url (str): URL to the YouTube movie trailer
    '''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    # Play movie trailer
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
