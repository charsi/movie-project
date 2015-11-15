import media
import fresh_tomatoes

reservoir_dogs = media.Movie(
    "Reservoir Dogs",
    "After a simple jewelery heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.",
    "http://i.imgur.com/1cmyEND.jpg",
    "https://www.youtube.com/watch?v=YNvLLKLwmwY",
    1992
    )

in_bruges = media.Movie(
    "In Bruges",
    "Guilt-stricken after a job gone wrong, hitman Ray and his partner await orders from their ruthless boss in Bruges, Belgium, the last place in the world Ray wants to be.",
    "http://www.impawards.com/2008/posters/in_bruges_ver2_xlg.jpg",
    "https://www.youtube.com/watch?v=bqOJqR1cjhI",
    2008
    )

def print_storyline(movie):
    print(movie.title+" ee :\n"+movie.storyline)

print_storyline(reservoir_dogs)
print(in_bruges.year)

##in_bruges.show_trailer()

movies = [reservoir_dogs, in_bruges]

fresh_tomatoes.open_movies_page(movies)

##print(media.Movie.__doc__)
##print(media.Movie.__name__)
##print(media.Movie.__module__)