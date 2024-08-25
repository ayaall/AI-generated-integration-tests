from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Patient

class PatientTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.patient = Patient.objects.create(user=self.user, Blood_Pressure='123')

    def test_patient_can_update_blood_pressure(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('update_blood_pressure_patient', args=[self.patient.id]), {'Blood_Pressure': '456'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'testuser')
        
        # Reload the patient from the database to check if the update was applied
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.Blood_Pressure, '456')
