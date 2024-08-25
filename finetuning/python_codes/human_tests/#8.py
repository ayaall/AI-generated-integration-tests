def test_update_kidney_function(self):
        """test_update_kidney_function """
        # accss view
        self.assertTrue(User.is_authenticated)
        response = self.client.get(('update-KidneyFunction/<int:id>'))

        self.assertNotEqual(response.status_code, 300)

        # logout
        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)
