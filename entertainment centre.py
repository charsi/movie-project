import media
import fresh_tomatoes

# Movie objects containing information on movies
# to be displayed in HTML page.
# Movie class defined in media module
reservoir_dogs = media.Movie(
    "Reservoir Dogs",
    "After a simple jewelery heist goes terribly wrong,"\
    " the surviving criminals begin to suspect that one of"\
    " them is a police informant.",
    "http://i.imgur.com/1cmyEND.jpg",
    "https://www.youtube.com/watch?v=YNvLLKLwmwY",
    "http://www.imdb.com/title/tt0105236",
    1992
)

in_bruges = media.Movie(
    "In Bruges",
    "Guilt-stricken after a job gone wrong, hitman Ray and"\
    " his partner await orders from their ruthless boss in"\
    " Bruges, Belgium, the last place in the world Ray wants"\
    " to be.",
    "http://www.impawards.com/2008/posters/in_bruges_ver2_xlg.jpg",
    "https://www.youtube.com/watch?v=bqOJqR1cjhI",
    "http://www.imdb.com/title/tt0780536",
    2008
)

kkg = media.Movie(
    "Khosla Ka Ghosla",
    "A Delhi based retired middle class man tries half-heartedly"\
    " to get his land back from a swindling property dealer with"\
    " the help of his sons and their friends.",
    "http://www.impawards.com/intl/india/2006/posters/khosla_ka_ghosla.jpg",
    "https://www.youtube.com/watch?v=jUy9ho06RuQ",
    "http://www.imdb.com/title/tt0466460",
    2006
)

gow2 = media.Movie(
    "Gangs Of Wasseypur",
    "A clash between Sultan (a Qureishi dacoit chief) and Shahid"\
    " Khan (a Pathan who impersonates him) leads to the expulsion"\
    " of Khan from Wasseypur, and ignites a deadly blood feud"\
    " spanning three generations.",
    "http://www.paragsankhe.com/wp-content/uploads/2013/01/"
    "Gangs-of-Wasseypur_UK_30x40_Coal_Poster.jpg",
    "https://www.youtube.com/watch?v=Z1nmIm5ncNE",
    "http://www.imdb.com/title/tt1954470",
    2012
)

monsoon_wedding = media.Movie(
    "Monsoon Wedding",
    "A stressed father, a bride-to-be with a secret, a"\
    " smitten event planner, and relatives from around"\
    " the world create much ado about the preparations"\
    " for an arranged marriage in India.",
    "http://www.amoeba.com/admin/uploads/blog/Eric_B/"\
    "monsoon_wedding_ver6_xlg.jpg",
    "https://www.youtube.com/watch?v=eaP-UrmS6Ww",
    "http://www.imdb.com/title/tt0265343",
    2001
)

true_romance = media.Movie(
    "True Romance",
    "Clarence marries hooker Alabama, steals cocaine"\
    " from her pimp, and tries to sell it in Hollywood,"\
    " while the owners of the coke try to reclaim it.",
    "http://cdn-images.9cloud.us/22/"\
    "piccit_true_romance_1993_1534_x_217_2069657734.jpg",
    "https://www.youtube.com/watch?v=_wNYNDzKpuQ",
    "http://www.imdb.com/title/tt0108399/",
    1993
)

ollo = media.Movie(
    "Oye Lucky Lucky Oye",
    "A burglar reflects on his life and loves; while"\
    " the media speculates how he managed to pull off so many heists.",
    "http://www.impawards.com/intl/india/2008/posters/oye_lucky_lucky_oye.jpg",
    "https://www.youtube.com/watch?v=3paPF30NJhg",
    "http://www.imdb.com/title/tt1292703/",
    1993
)

# Movies to be included on the page
movies = [
    reservoir_dogs,
    in_bruges,
    kkg, gow2,
    monsoon_wedding,
    true_romance,
    ollo
]

# Create HTML page and launch it in default web browser
fresh_tomatoes.open_movies_page(movies)
