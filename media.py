import webbrowser

class Movie():
    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, title, star, story, poster, trailer):
        # create instance variables
        self.title = title
        self.star = star
        self.storyline = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    # open trailer
    def show_trailer(self):
      webbrowser.open(self.trailer)