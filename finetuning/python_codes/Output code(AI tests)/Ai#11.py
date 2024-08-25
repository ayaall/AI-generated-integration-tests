from django.test import TestCase
from django.urls import resolve
from .views import map_view  # Adjust the import based on your views

class TestUrls(TestCase):

    def test_map_view_url_is_correct(self):
        """Test that the map_view URL is correctly resolved to the map_view function."""
        url = '/map/'
        resolved = resolve(url)
        self.assertEqual(resolved.func, map_view)
