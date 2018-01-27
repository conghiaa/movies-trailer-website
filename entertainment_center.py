import media
import fresh_tomatoes

# Toy Story movie: movie title, storyline, poster image and movie trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",  # NOQA
    "https://www.youtube.com/watch?v=TNMpa5yBf5o"
)

# Avatar movie: movie title, storyline, poster image and movie trailer
avatar = media.Movie(
    "Avatar",
    "A marine on a alien planet",
    "http://cafmp.com/wp-content/uploads/2012/12/Avatar-Neytiri.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6ziBFh3V1aM"
)

# One Day movie: movie title, storyline, poster image and movie trailer
one_day = media.Movie(
    "One Day",
    "After spending the night together on the night of their college graduation\
     Dexter  and Em reunite each year on the same date to see where they are \
     in their lives...",
    "http://images5.fanpop.com/image/photos/25000000/One-Day-Poster-one-day-2011-movie-25098386-350-500.jpg",  # NOQA
    "https://www.youtube.com/watch?v=nk8W8DyZBiU"
)

# A list of the movies passed to the open_movies_page function as a paramater.
movies = [toy_story, avatar, one_day]

# Calling this function will create and open the HTML file in a browser
# to visitors
fresh_tomatoes.open_movies_page(movies)
