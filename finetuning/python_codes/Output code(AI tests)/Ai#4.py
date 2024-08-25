from django.test import TestCase
from django.contrib.auth.models import User
from .models import Patient
from .views import patient_dashboard

class PatientDashboardTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.patient = Patient.objects.create(user=self.user, age=20)

    def test_patient_dashboard(self):
        response = self.client.get('/patient_dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient_dashboard.html')
        self.assertContains(response, self.patient.age)
