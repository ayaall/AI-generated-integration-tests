   def test_login_and_patient_book_appointment_and_logout(self):
        """test_login_and_patient_book_appointment_and_logout """
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(User.is_authenticated)

        response = self.client.get(('bookappointment'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)