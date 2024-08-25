from django.test import TestCase
from django.urls import resolve

from.views import nurse_dashboard

class TestUrls(TestCase):
    def test_nurse_dashboard_url_is_correct(self):
        url = resolve('/nurse_dashboard/').url
        self.assertEqual(url, '/nurse_dashboard/')
