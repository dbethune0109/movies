import webbrowser

class Movie():
    """VALID_RATING G, PG, PG13,  R"""
def __init__(udacity, movie_title, movie_storyline, poster_image, trailer_youtube):
        udacity.title = movie_title
        udacity.storyline = movie_storyline
        udacity.poster_image_url = poster_image
        udacity.trailer_youtube_url = trailer_youtube

def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
print Movie. __doc__
