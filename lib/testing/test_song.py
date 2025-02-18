import unittest
from lib.song import Song

class TestSongClass(unittest.TestCase):
    
    def setUp(self):
        """Reset class attributes before each test."""
        Song.count = 0
        Song.artists = []
        Song.genres = []
        Song.genre_count = {}
        Song.artist_count = {}

    def test_song_class_count(self):
        """Test if the class attribute count is correctly updated."""
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Hotline Bling", "Drake", "Pop")
        song3 = Song("Formation", "Beyoncé", "Pop")
        
        self.assertEqual(Song.count, 3)  # 3 songs should have been created

    def test_song_class_artists(self):
        """Test if the artists list is correctly populated."""
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Hotline Bling", "Drake", "Pop")
        song3 = Song("Formation", "Beyoncé", "Pop")
        
        self.assertEqual(Song.artists, ["Jay-Z", "Drake", "Beyoncé"])

    def test_song_class_genres(self):
        """Test if the genres list is correctly populated."""
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Hotline Bling", "Drake", "Pop")
        song3 = Song("Formation", "Beyoncé", "Pop")
        
        self.assertEqual(Song.genres, ["Rap", "Pop"])

    def test_song_class_genre_count(self):
        """Test if the genre count dictionary is correct."""
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Hotline Bling", "Drake", "Pop")
        song3 = Song("Formation", "Beyoncé", "Pop")
        
        self.assertEqual(Song.genre_count, {"Rap": 1, "Pop": 2})

    def test_song_class_artist_count(self):
        """Test if the artist count dictionary is correct."""
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        song2 = Song("Hotline Bling", "Drake", "Pop")
        song3 = Song("Formation", "Beyoncé", "Pop")
        
        self.assertEqual(Song.artist_count, {"Jay-Z": 1, "Drake": 1, "Beyoncé": 1})

    def test_song_attributes(self):
        """Test if the song attributes are correctly set."""
        song1 = Song("99 Problems", "Jay-Z", "Rap")
        self.assertEqual(song1.name, "99 Problems")
        self.assertEqual(song1.artist, "Jay-Z")
        self.assertEqual(song1.genre, "Rap")

if __name__ == "__main__":
    unittest.main()
