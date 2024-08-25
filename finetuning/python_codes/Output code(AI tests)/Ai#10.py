from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Appointment  # Ensure you import the correct models
from .views import admin_book_appointment

class TestAdminBookAppointment(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.client.login(username='admin', password='admin')

    def test_admin_book_appointment(self):
        response = self.client.post(reverse('admin_book_appointment'), {
            'appointment': '2022-05-15',
            'time': '12:30'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AdminBookAppointment.html')
        self.assertContains(response, 'Book Success')
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(Appointment.objects.first().date, '2022-05-15')
        self.assertEqual(Appointment.objects.first().time, '12:30')

    def test_admin_book_appointment_invalid(self):
        response = self.client.post(reverse('admin_book_appointment'), {
            'appointment': '2022-05-15',
            'time': '12:30'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AdminBookAppointment.html')
        self.assertContains(response, 'Book Success')  # Modify this based on the actual error handling in your view
        self.assertEqual(Appointment.objects.count(), 1)  # Ensure this count matches your scenario

        # Additional checks if the response should indicate an error
        # self.assertContains(response, 'Error message')  # Example placeholder, adjust as necessary
