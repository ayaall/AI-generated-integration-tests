 def test_map(self):
        """test_map """
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(User.is_authenticated)

        response = self.client.get(('map'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)