import media
import fresh_tomatoes

# NCS Cartoon on and on song : title, description, poster image, video song url
NCS_cartoon_on_and_on = media.Song(
    "NCS Cartoon on&on",
    "Cool song",
    "ncs_on_nd_on.jpg",
    "https://www.youtube.com/watch?v=K4DyBUG242c"
    )

# Starset:It has begun song : title, description, poster image, video song url
starset_it_has_begun = media.Song(
    "It has begun",
    "Starset 1",
    "starset_it_has_begun.jpg",
    "https://www.youtube.com/watch?v=O1asGKxmS34"
    )

# Starset:My Demons song : title, description, poster image, video song url
starset_my_demons = media.Song(
    "My Demons",
    "Starset 2",
    "mydemons.jpg",
    "https://www.youtube.com/watch?v=LSvOTw8UH6s"
    )

# Starset:carnivore song : title, description, poster image, video song url
starset_carnivore = media.Song(
    "Carnovore",
    "Starset 3",
    "starset_carnivore.jpg",
    "https://www.youtube.com/watch?v=LAMiX5EEbFU"
    )

# One Piece Anime sound track 1: title, description, poster image, song url
one_piece_epic_theme = media.Song(
    "One Piece Epic Battle theme",
    "Soundtrack at another level 1",
    "one-piece-poster-shanks.jpg",
    "https://www.youtube.com/watch?v=4J7K3yacig4"
    )

# One Piece Anime sound track 2: title, description, poster image, song url
one_piece_ost_overtaken = media.Song(
    "One Piece OST Overtaken",
    "Soundtrack at another level 2",
    "one_piece_overtaken.jpg",
    "https://www.youtube.com/watch?v=daFi4MScfl8"
    )

# Doublemint:Ek ajanabi Haseenase : title, description, poster image, song url
ek_ajnabi_haseena_se = media.Song(
    "Ek Ajnabi Haseens se",
    "Love song 1",
    "ek ajnabi haseens se.jpg",
    "https://www.youtube.com/watch?v=e5BbHPHpbvE"
    )

# List of all music/track instaces
music = [
    NCS_cartoon_on_and_on,
    starset_it_has_begun,
    starset_my_demons,
    starset_carnivore,
    one_piece_epic_theme,
    one_piece_ost_overtaken,
    ek_ajnabi_haseena_se
    ]

# pass track list to fresh_tomatoes.py to generate web page
fresh_tomatoes.open_movies_page(music)
