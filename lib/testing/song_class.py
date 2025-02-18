class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call the class methods to update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre if not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist if not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Test the functionality with some sample songs
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Hotline Bling", "Drake", "Pop")
song3 = Song("Run the World", "Beyonce", "Pop")
song4 = Song("Numb", "Jay-Z", "Rap")
song5 = Song("Bohemian Rhapsody", "Queen", "Rock")

# Checking the results
print(Song.count)  # Number of songs created
print(Song.artists)  # List of unique artists
print(Song.genres)  # List of unique genres
print(Song.genre_count)  # Count of songs by genre
print(Song.artist_count)  # Count of songs by artist
