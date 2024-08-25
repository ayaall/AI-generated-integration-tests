from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Nurse, Patient, Record

class TestNurseAddRecord(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='nurseuser', password='password')
        self.nurse = Nurse.objects.create(user=self.user, name='Nurse Name')
        self.patient = Patient.objects.create(name='Patient Name')
        self.record = Record.objects.create(body='Record Body', patient=self.patient, nurse=self.nurse)

    def test_nurse_add_record(self):
        """Test Nurse Add Record"""
        self.client.force_login(self.user)
        response = self.client.post(reverse('nurse_record'), {
            'patientName': self.patient.name,
            'body': 'New Record Body',
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertEqual(Record.objects.count(), 2)  # Check that a new record was added
        self.assertTrue(Record.objects.filter(body='New Record Body').exists())  # Check that the record exists

