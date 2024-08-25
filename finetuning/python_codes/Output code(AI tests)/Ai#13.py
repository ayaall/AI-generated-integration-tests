from django.test import TestCase
from django.urls import reverse
from .models import Patient

class TestUpdateUrineSurgery(TestCase):
    def setUp(self):
        # Create a Patient instance with initial data
        self.patient = Patient.objects.create(user_id=1, Urine_surgery="urine surgery")

    def test_update_urine_surgery(self):
        # Log in as a user if authentication is required (adjust as necessary)
        # self.client.login(username='testuser', password='password')

        # Perform a POST request to update the Urine_surgery field
        response = self.client.post(
            reverse('update_urine_surgery'),
            data={'user_id': self.patient.user_id, 'Urine_surgery': 'urine surgery updated'}
        )
        
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Refresh the patient instance from the database to get updated data
        self.patient.refresh_from_db()
        
        # Verify that the Urine_surgery field was updated correctly
        self.assertEqual(self.patient.Urine_surgery, 'urine surgery updated')
