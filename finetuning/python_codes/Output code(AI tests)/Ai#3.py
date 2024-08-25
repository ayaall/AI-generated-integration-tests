def test_afterlogin_view(self):
    self.client.login(username='testuser', password='testpassword')
    response = self.client.get(reverse('afterlogin_view'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'loginPage.html')
    self.client.logout()

    response = self.client.post(reverse('afterlogin_view'), {'username': 'testuser', 'password': 'testpassword'})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'loginPage.html')
    self.client.logout()

    response = self.client.post(reverse('afterlogin_view'), {'username': 'testuser', 'password': 'testpassword'})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'loginPage.html')
    self.client.logout()
