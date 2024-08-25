from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse

class CreatePostTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

    def test_create_post(self):
        response = self.client.post(reverse('createPost'), data={
            'title': 'test title',
            'body': 'test body',
            'author': self.user.id  # Adjust this if your form expects user ID instead of User object
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.get()
        self.assertEqual(post.title, 'test title')
        self.assertEqual(post.body, 'test body')
        self.assertEqual(post.author, self.user)
