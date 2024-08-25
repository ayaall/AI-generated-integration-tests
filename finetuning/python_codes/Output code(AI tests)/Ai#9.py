from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Appointment
from .views import book_appointment

class TestAppointment(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')
        self.user.save()
        self.appointment = Appointment.objects.create(
            date='2022-05-01',
            time='12:00',
            name='test',
            patient_id=self.user.id  # Assuming patient_id should refer to the user created
        )
        self.appointment.save()

    def test_book_appointment(self):
        # Test GET request for booking appointment
        response = self.client.get('/book_appointment/')
        self.assertEqual(response.status_code, 200)

        # Test POST request with already booked appointment
        response = self.client.post('/book_appointment/', 
                                    data={'appointment': '2022-05-01', 
                                          'time': '12:00'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book_appointment/')

        # Test POST request with the same appointment time
        response = self.client.post('/book_appointment/', 
                                    data={'appointment': '2022-05-01', 
                                          'time': '12:00'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], 
                         "The role is already booked")

        # Test POST request with a different time on the same day
        response = self.client.post('/book_appointment/', 
                                    data={'appointment': '2022-05-01', 
                                          'time': '13:00'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book_appointment/')

        # Test POST request with a different day
        response = self.client.post('/book_appointment/', 
                                    data={'appointment': '2022-05-02', 
                                          'time': '12:00'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book_appointment/')

        # Test POST request with a different time on a different day
        response = self.client.post('/book_appointment/', 
                                    data={'appointment': '2022-05-02', 
                                          'time': '13:00'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book_appointment/')
