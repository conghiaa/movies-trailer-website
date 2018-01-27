class Movie(object):
    """A collection of movies"""

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """Constructor takes in movie title, storyline, poster image's url
        and trailer youtube's url and create an instance of this class."""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
