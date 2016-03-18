import fresh_tomatoes
import media

# define movies using media.Movie instances
pulp_fiction = media.Movie("Pulp Fiction", "Samuel L. Jackson", "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper.", "http://a1.mzstatic.com/us/r30/Video3/v4/b7/30/8b/b7308b8f-d9ce-41fc-928a-76a87de7d966/poster227x227.jpeg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
birdman = media.Movie("Birdman", "Michael Keaton", "A fading actor best known for his portrayal of a popular superhero attempts to mount a comeback by appearing in a Broadway play.", "http://oblivion.a.ltrbxd.com/resized/film-poster/1/3/9/7/9/5/139795-birdman-0-460-0-690-crop.jpg?k=5aee70e478", "https://www.youtube.com/watch?v=2bqh-UCY6Zg")
shawshank = media.Movie("The Shawshank Redemption", "Tim Robbins", "FEAR CAN HOLD YOU PRISONER. HOPE CAN SET YOU FREE.", "http://skyfall.a.ltrbxd.com/resized/film-poster/5/1/7/7/8/51778-the-shawshank-redemption-0-460-0-690-crop.jpg?k=eedbde1cef", "https://www.youtube.com/watch?v=WawU4ouldxU")

# create list of movies
movies = [pulp_fiction, birdman, shawshank]

# generate HTML using fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)