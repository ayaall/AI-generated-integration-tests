from django.test import TestCase
from django.urls import reverse
from.models import Category
from.forms import Categoryform
from django.contrib.auth.models import User

class CategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a superuser for testing
        user = User.objects.create_user(username='testuser', password='12345')
        user.is_superuser = True
        user.save()
        # Create a test category
        cls.category = Category.objects.create(name='testcategory', description='testdesc')

    def test_edit_category(self):
        # Log in as the superuser
        self.client.login(username='testuser', password='12345')
        
        # Get request for the edit category page
        response = self.client.get(reverse('edit_category', args=[self.category.pk]))
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Post request to update the category
        response = self.client.post(reverse('edit_category', args=[self.category.pk]), {
            'name': 'newcategory',
            'description': 'newdesc'
        })
        # Check that the status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)
        
        # Get request to verify the updated data
        response = self.client.get(reverse('edit_category', args=[self.category.pk]))
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the form's initial values are updated
        self.assertEqual(response.context['form'].initial['name'], 'newcategory')
        self.assertEqual(response.context['form'].initial['description'], 'newdesc')
        
        # Log out the user
        self.client.logout()
        # Get request after logout to verify form values persist
        response = self.client.get(reverse('edit_category', args=[self.category.pk]))
        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check that the form's initial values are still correct
        self.assertEqual(response.context['form'].initial['name'], 'newcategory')
        self.assertEqual(response.context['form'].initial['description'], 'newdesc')
