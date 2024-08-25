def test_categories(self):
        response = self.client.get(self.categories_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.categories_url)
        self.assertTemplateUsed("categoryFormPage")

        response = self.adminclient.post(self.categories_url ,data ={'name':'categor'},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("categoryFormPage")