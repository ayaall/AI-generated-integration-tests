from django.test import TestCase
from django.contrib.auth.models import User
from . import models

class TestUpdateECG(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.patient = models.Patient.objects.create(user_id=self.user, ECG='test')

    def test_update_ecg(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/updateECG', {'ECG': 'updated test'})
        self.assertEqual(response.status_code, 200)
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.ECG, 'updated test')
