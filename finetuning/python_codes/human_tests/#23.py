  def test_editCategory(self):
        response = self.client.get(self.editCategory_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("admin_error.html")
        
        response = self.adminclient.get(self.editCategory_url)
        self.assertTemplateUsed("categoryFormPage")
        
        response = self.adminclient.post(self.editCategory_url ,data ={'name':'categor'},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("categoryFormPage")
