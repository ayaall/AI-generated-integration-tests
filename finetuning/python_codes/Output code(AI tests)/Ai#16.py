def test_myPosts(self):
    """Test the myPosts view"""
    user = HelpoUser.objects.get(user_id=1)  # Adjust `user_id` as needed for your test
    self.client.force_login(user.user)
    
    response = self.client.get(reverse('myPosts', kwargs={'pk': user.user_id}))
    
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'myPosts.html')
    self.assertIn('posts', response.context)
    self.assertIn('user_obj', response.context)
