import webbrowser


class Song():
    """This class stores songs information"""
    def __init__(self, song_title, song_desc, song_img_url, song_trailer_link):
        self.title = song_title
        self.storyline = song_desc
        self.poster_image_url = song_img_url
        self.trailer_youtube_url = song_trailer_link
