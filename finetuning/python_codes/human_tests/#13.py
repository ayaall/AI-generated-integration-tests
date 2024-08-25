 def test_urine_surgery(self):
        """test_urine_surgery """
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(User.is_authenticated)

        response = self.client.get(('update-Urine-surgery'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)