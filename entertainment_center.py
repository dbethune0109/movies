import fresh_tomatoes
import media
    # Toy Story info #
toy_story = media.Movie("Toy Story",
                            "A story of a boy and his toys that come to life",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    # John Wick Info #
john_wick = media.Movie("John Wick",
                            "An ex-hitman comes out of retirement to track down the gangsters that took everything from him.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
    # John Wick 2 Info #
john_wick2 = media.Movie("John Wick 2",
                            "Hitman John Wick is forced out of retirement by a former associate plotting to seize control of an international assassins' guild. Bound by a blood oath to help him, John travels to Rome where he squares off against the world's deadliest killers.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxMzc4MTkwOF5BMl5BanBnXkFtZTgwOTE5MDcyMDI@._V1_UY268_CR3,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=XGk2EfbD_Ps")
    # Star Wars A new hope info #
star_wars = media.Movie("Star Wars",
                            "Star Wars is an American epic space opera franchise, centered on a film series created by George Lucas. It depicts the adventures of various characters, a long time ago in a galaxy far, far away",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZGEzZTExMDEtNjg4OC00NjQxLTk5NTUtNjRkNjA3MmYwZjg1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=1g3_CFmnU7k")
    # creates array of movies to be called #
movies = [toy_story, john_wick, john_wick2, star_wars]
    # creates list in html file(fresh_tomatoes) #
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATING)    

