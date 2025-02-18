class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Initialize the song with its attributes and update class attributes."""
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the song count when a new song is created
        Song.count += 1
        
        # Add the artist and genre to their respective lists and counts
        self.add_to_artists()
        self.add_to_genres()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_to_artists(self):
        """Add the artist to the artists list if it's not already present."""
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genres(self):
        """Add the genre to the genres list if it's not already present."""
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_genre_count(self):
        """Update the genre count in the genre_count dictionary."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        """Update the artist count in the artist_count dictionary."""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
