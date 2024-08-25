from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Nurse, Food


class TestNurse(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='12345',
        )

        self.nurse = Nurse.objects.create(
            user=self.user,
            name="testname",
            age=25,
            address="testaddress",
            phone="testphone",
            pin="testpin",
            role="testrole",
            username="testusername",
            password="testpassword",
            gender="testgender",
            hospital="testhospital",
            department="testdepartment",
            experience="testexperience",
            description="testdescription",
            image="testimage",
        )

        self.nurse.save()

        self.food = Food.objects.create(
            Name="testName",
            number="testnumber",
            max_Cholesterol="testmax_Cholesterol",
            max_Liver_function="testmax_Liver_function",
            max_Kidney_function="testmax_Kidney_function",
            max_Blood_Pressure="testmax_Blood_Pressure",
            pic="testpic",
        )

        self.food.save()

    def test_nurse_view_food(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('nurse_view_food'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nurse_view_food.html')

    def test_nurse_add_food(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('nurse_add_food'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nurse_add_food.html')

        response = self.client.post(reverse('nurse_add_food'), data={
            'Name': 'testName',
            'num': 'testnum',
            'max_Cholesterol': 'testmax_Cholesterol',
            'max_Liver_function': 'testmax_Liver_function',
            'max_Kidney_function': 'testmax_Kidney_function',
            'max_Blood_Pressure': 'testmax_Blood_Pressure',
            'pic': SimpleUploadedFile(name='testpic', content=b'file_content', content_type='image/png'),
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nurse_add_food.html')

        response = self.client.post(reverse('nurse_add_food'), data={
            'Name': 'testName',
            'num': 'testnum',
            'max_Cholesterol': 'testmax_Cholesterol',
            'max_Liver_function': 'testmax_Liver_function',
            'max_Kidney_function': 'testmax_Kidney_function',
            'max_Blood_Pressure': 'testmax_Blood_Pressure',
            'pic': SimpleUploadedFile(name='testpic', content=b'file_content', content_type='image/png'),
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nurse_add_food.html')
