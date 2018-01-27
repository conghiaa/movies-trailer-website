import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=TNMpa5yBf5o")

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://cafmp.com/wp-content/uploads/2012/12/Avatar-Neytiri.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
one_day = media.Movie("One Day",
					"After spending the night together on the night of their college graduation Dexter  and Em reunite each year on the same date to see where they are in their lives...",
					"http://images5.fanpop.com/image/photos/25000000/One-Day-Poster-one-day-2011-movie-25098386-350-500.jpg",
					"https://www.youtube.com/watch?v=zVuuooZqVaU")

movies = [toy_story, avatar, one_day]



# movies = [
#     media.Movie("Peter Rabbit", "http://t0.gstatic.com/images?q=tbn:ANd9GcTv080sygzRHWCa1hnxhXKXQHtj39fhNKQ7x_exqn-2smPivgv-", "https://www.youtube.com/watch?v=dJQjNadiQHI"),
#     media.Movie("Here We Go Again", "https://i.ytimg.com/vi/1OCTv47XQpA/maxresdefault.jpg", "https://www.youtube.com/watch?v=wLXDrfgnBfI&index=18&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-"),
#     media.Movie("Sicario 2: Soldado Teaser", "https://i.ytimg.com/vi/4br1A1tltkc/maxresdefault.jpg", "https://www.youtube.com/watch?v=4br1A1tltkc&index=19&list=PLScC8g4bqD47c-qHlsfhGH3j6Bg7jzFy-")
# ]
fresh_tomatoes.open_movies_page(movies)
