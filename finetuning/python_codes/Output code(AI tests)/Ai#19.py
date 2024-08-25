import pytest
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse
from.forms import FeedbackForm
from.models import Feedback
from.views import sendFeedback

class TestFeedback(TestCase):
    def test_sendFeedback(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', email='test@user.com', password='test_password')
        self.user.is_helpo_user = True
        self.user.is_association_manager = True
        self.user.save()

        self.client.login(username='test_user', password='test_password')
        response = self.client.post(reverse('sendFeedback'), {'feedback': 'test_feedback'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sendFeedback.html')
        self.assertContains(response, 'test_feedback')
        self.assertContains(response, 'test_user')

        self.client.login(username='test_user', password='test_password')
        response = self.client.post(reverse('sendFeedback'), {'feedback': 'test_feedback'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error_page.html')
        self.assertContains(response, 'You are already a user of Helpo.')

        self.client.login(username='test_user', password='test_password')
        response = self.client.post(reverse('sendFeedback'), {'feedback': 'test_feedback'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sendFeedback.html')
        self.assertContains(response, 'test_feedback')
        self.assertContains(response, 'test_user')
