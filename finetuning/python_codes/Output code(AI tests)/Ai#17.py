from django.urls import reverse
from django.test import TestCase

from.models import HelpoUser, Post
from.forms import createPostForm

class EditPostTest(TestCase):
    def setUp(self):
        self.user = HelpoUser.objects.create(user='test', username='test')
        self.post = Post.objects.create(user=self.user, post='test')

    def test_editPost(self):
        response = self.client.post(reverse('editPost', kwargs={'pk': self.post.id}), {'post': 'updated'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.get(pk=self.post.id).post, 'updated')
