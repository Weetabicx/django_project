import importlib
from django.test import TestCase

# Create your tests here.
HEADER = "\n\n==============================!"
FOOTER = "!==============================\n"
class AlbumModelsTestCase(TestCase):
    """Tests for the album models, this test assume the populaton script has been runs."""

    def setUp(self,):
        pass


class AlbumViewsTestCase(TestCase):
    """Tests for the album models and views, this test assume the populaton script has been runs."""

    def setUp(self,):
        self.views_module = importlib.import_module('album.views')
        self.views_module_listing = dir(self.views_module)

    def test_views_exist(self,):
        """Test that the correct views exists."""
        views = ['albums_list', 'upload_album', 'album_update', 'album_delete', 'album_detail']
        for view in views:
            self.assertIn(view, self.views_module_listing, f"{HEADER}View {view} not found in views module.{FOOTER}")
