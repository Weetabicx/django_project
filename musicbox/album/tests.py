import importlib
from django.test import TestCase
from album.models import Album, Album_Comment
from song.models import Song
from django.contrib.auth.models import User
from django.urls import reverse

HEADER = "\n\n==============================!"
FOOTER = "!==============================\n"

class AlbumModelsTestCase(TestCase):
    """Tests for the album models"""

    def setUp(self,):
        User.objects.create(username="testuser", password="testpassword")
        test_album_1 = Album.objects.create(name="Test Album1", type="Album", genre="Rock", release_date="2020-01-01", artist="Test Artist", owner_id=1)
        test_single = Album.objects.create(name="Test Single", type="Single", genre="Rock", release_date="2020-01-02", artist="Test Artist", owner_id=1)
        test_ep = Album.objects.create(name="Test EP", type="EP", genre="Rock", release_date="2020-01-03", artist="Test Artist", owner_id=1)
        test_album_2 = Album.objects.create(name="Test Album2", type="Album", genre="Rock", release_date="2020-01-04", artist="Test Artist", owner_id=1)
        test_album_3 = Album.objects.create(name="Test Album3", type="Album", genre="Rock", release_date="2020-01-05", artist="Test Artist", owner_id=1)

        
        Album_Comment.objects.create(album=test_album_1, rating=1, comment="Test Comment")
        Album_Comment.objects.create(album=test_album_2, rating=2, comment="Test Comment")
        Album_Comment.objects.create(album=test_album_3, rating=3, comment="Test Comment")
        Album_Comment.objects.create(album=test_single, rating=4, comment="Test Comment")
        Album_Comment.objects.create(album=test_ep, rating=5, comment="Test Comment")

    def test_albums_exist(self,):
        """Test that the albums exists."""
        self.assertEqual(Album.objects.count(), 5, f"{HEADER}Expected 5 albums, found {Album.objects.count()}.{FOOTER}")

    def test_album_top(self,):
        """Test that the top_albums method returns the top albums."""
        expected = [3,2,5,4,1]
        for i, album in enumerate(Album.top_albums()):
            self.assertEqual(album[0].id, expected[i], f"{HEADER}Expected album {Album.objects.get(id=expected[i])}, found {album}.{FOOTER}")

    def test_album_latest(self,):
        """Test that the latest_albums method returns the latest albums."""
        expected = [5,4,3,2,1]
        for i, album in enumerate(Album.latest_albums()):
            self.assertEqual(album.id, expected[i], f"{HEADER}Expected album {Album.objects.get(id=expected[i])}, found {album}.{FOOTER}")

class AlbumViewsTestCase(TestCase):
    """Tests for the album models and views"""

    def setUp(self,):
        self.views_module = importlib.import_module('album.views')
        self.views_module_listing = dir(self.views_module)
        User.objects.create(username="testuser", password="testpassword")

        Album.objects.create(name="Test EP", type="EP", genre="Rock", release_date="2020-01-03", artist="Test Artist", owner_id=1)


    def test_views_exist(self,):
        """Test that the correct views exists."""
        views = ['albums_list', 'upload_album', 'album_update', 'album_delete', 'album_detail']
        for view in views:
            self.assertIn(view, self.views_module_listing, f"{HEADER}View {view} not found in views module.{FOOTER}")
    
    def test_albums_list(self,):
        """Test that the albums_list view has the correct data"""
        response = self.client.get('/albums/albums_list')
        self.assertIn("Test EP", response.content.decode('utf-8'), f"{HEADER}Expected Test EP in response, found {response.content.decode('utf-8')}.{FOOTER}")

    # TODO : Need to login to test this    
    # def test_albums_upload(self,):
    #     """Test that the upload_album view works"""
    #     response = self.client.post('/albums/upload_album/', {'name': 'Test Album', 'type': 'Album', 'genre': 'Rock', 'release_date': '2020-01-01', 'artist': 'Test Artist', 'owner': 1})
    #     self.assertEqual(response.status_code, 200, f"{HEADER}Expected status code 200, found {response.status_code}.{FOOTER}")
    
    def test_albums_update(self,):
        """Test that the album_update view works"""
        response = self.client.post('/albums/album/1/update/', {'name': 'Test Album', 'type': 'Album', 'genre': 'Rock', 'release_date': '2020-01-01', 'artist': 'Test Artist'})
        print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200, f"{HEADER}Expected status code 200, found {response.status_code}.{FOOTER}")
    