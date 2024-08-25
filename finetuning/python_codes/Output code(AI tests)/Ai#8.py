from unittest.mock import Mock
from django.test import TestCase

# Assuming the function `update_kidney_function` is imported from your views
from .views import update_kidney_function

class UpdateKidneyFunctionTest(TestCase):
    def test_update_kidney_function(self):
        # Given
        request = Mock()
        request.method = 'POST'
        request.POST['KidneyFunction'] = 'Kidney Function'
        id_ = 1
        
        # When
        response = update_kidney_function(request, id_)
        
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTrue('KidneyFunction' in request.POST)
        self.assertEqual(request.POST['KidneyFunction'], 'Kidney Function')
