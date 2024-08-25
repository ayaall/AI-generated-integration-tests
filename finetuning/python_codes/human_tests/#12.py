   def test_nurse_add_record(self):
        """test_nurse_add_record """
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(User.is_authenticated)

        response = self.client.get(('admin-nurse-reprot'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)
