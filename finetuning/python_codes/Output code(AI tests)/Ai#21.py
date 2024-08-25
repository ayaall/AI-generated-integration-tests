from django.test import TestCase
from django.urls import resolve, reverse
from .views import deletePhoto
from .models import Image, Association
from django.contrib.auth.models import User

class DeletePhotoTest(TestCase):
    def setUp(self):
        self.asso = Association.objects.create(name='test association')
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.user.is_superuser = True
        self.user.save()
        self.asso.manager = self.user
        self.asso.save()

        self.photo = Image.objects.create(association=self.asso, url='http://example.com/photo.jpg')

    def test_delete_photo(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('deletePhoto', args=(self.asso.pk, self.photo.pk))
        response = self.client.get(url)
        self.assertRedirects(response, reverse('associationPhotos', args=(self.asso.pk,)))

        self.photo.delete()
        self.assertFalse(Image.objects.filter(pk=self.photo.pk).exists())

    def test_delete_photo_not_manager(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('deletePhoto', args=(self.asso.pk, self.photo.pk))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'error_page.html')

        self.photo.delete()
        self.assertTrue(Image.objects.filter(pk=self.photo.pk).exists())

    def test_delete_photo_not_superuser(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('deletePhoto', args=(self.asso.pk, self.photo.pk))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'error_page.html')

        self.photo.delete()
        self.assertTrue(Image.objects.filter(pk=self.photo.pk).exists())

    def test_delete_photo_invalid_id(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('deletePhoto', args=(self.asso.pk, 99999))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'admin_error.html')

        self.photo.delete()
        self.assertTrue(Image.objects.filter(pk=self.photo.pk).exists())

    def test_delete_photo_invalid_association(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('deletePhoto', args=(99999, self.photo.pk))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'admin_error.html')

        self.photo.delete()
        self.assertTrue(Image.objects.filter(pk=self.photo.pk).exists())

    def test_delete_photo_invalid_photo(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('deletePhoto', args=(self.asso.pk, 99999))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'admin_error.html')

        self.photo.delete()
        self.assertTrue(Image.objects.filter(pk=self.photo.pk).exists())

    def test_delete_photo_url(self):
        found = resolve('/asso/1/photos/1/delete/').func
        self.assertEqual(found, deletePhoto)
