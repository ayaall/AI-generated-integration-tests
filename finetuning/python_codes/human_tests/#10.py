def test_login_and_admin_book_appointment_and_logout(self):
        """test_login_and_admin_book_appointment_and_logout """
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(User.is_authenticated)

        response = self.client.get(('adminbookappointment'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)