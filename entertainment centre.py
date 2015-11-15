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

kkg = media.Movie(
    "Khosla Ka Ghosla",
    "A Delhi based retired middle class man tries half-heartedly to get his land back from a swindling property dealer with the help of his sons and their friends.",
    "http://www.impawards.com/intl/india/2006/posters/khosla_ka_ghosla.jpg",
    "https://www.youtube.com/watch?v=jUy9ho06RuQ",
    2006
    )

gow2 = media.Movie(
    "Gangs Of Wasseypur",
    " A clash between Sultan (a Qureishi dacoit chief) and Shahid Khan (a Pathan who impersonates him) leads to the expulsion of Khan from Wasseypur, and ignites a deadly blood feud spanning three generations.",
    "http://www.paragsankhe.com/wp-content/uploads/2013/01/Gangs-of-Wasseypur_UK_30x40_Coal_Poster.jpg",
    "https://www.youtube.com/watch?v=Z1nmIm5ncNE",
    2012
    )

monsoon_wedding = media.Movie(
    "Monsoon Wedding",
    "A stressed father, a bride-to-be with a secret, a smitten event planner, and relatives from around the world create much ado about the preparations for an arranged marriage in India.",
    "http://www.amoeba.com/admin/uploads/blog/Eric_B/monsoon_wedding_ver6_xlg.jpg",
    "https://www.youtube.com/watch?v=eaP-UrmS6Ww",
    2001
    )

def print_storyline(movie):
    print(movie.title+" ee :\n"+movie.storyline)

print_storyline(reservoir_dogs)
print(in_bruges.year)

##in_bruges.show_trailer()

movies = [reservoir_dogs, in_bruges, kkg, gow2, monsoon_wedding]

fresh_tomatoes.open_movies_page(movies)

##print(media.Movie.__doc__)
##print(media.Movie.__name__)
##print(media.Movie.__module__)