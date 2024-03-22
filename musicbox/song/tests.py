import importlib
from django.test import TestCase
from song.models import Song
from album.models import Album
from django.contrib.auth.models import User
from album.tests import HEADER, FOOTER

class SongModelsTestCase(TestCase):
    """Tests for the song models"""

    def setUp(self,):
        user = User.objects.create(username="testuser", password="testpassword")
        album = Album.objects.create(name="Test Album", type="Album", genre="Rock", release_date="2020-01-01", artist="Test Artist", owner=user)
        for i in range(5):
            Song.objects.create(title=f"Test Song {i}", album=album, genre="Rock", release_date="2020-01-01", artist="Test Artist")
    
    def test_songs_exist(self,):
        """Test that the songs exists."""
        self.assertEqual(Song.objects.count(), 5, f"{HEADER}Expected 5 songs, found {Song.objects.count()}.{FOOTER}")    

class SongViewsTestCase(TestCase):

    def setUp(self,):
        user = User.objects.create(username="testuser", password="testpassword")
        album = Album.objects.create(name="Test Album", type="Album", genre="Rock", release_date="2020-01-01", artist="Test Artist", owner=user)
        song = Song.objects.create(title="Test Song", album=album, genre="Rock", release_date="2020-01-01", artist="Test Artist")

        self.views_module = importlib.import_module('song.views')
        self.views_module_listing = dir(self.views_module)
        
    def test_views_exist(self,):
        """Test that the correct views exists."""
        views = ['song_list_view', 'upload_song', 'delete_song']
        for view in views:
            self.assertIn(view, self.views_module_listing, f"{HEADER}View {view} not found in views module.{FOOTER}")