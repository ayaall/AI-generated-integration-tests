 def test_edit_association(self):
        #need to be loged in to asoo manager
        self.client.login(username="username",password="password")

        response = self.client.get(self.edit_association_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.assoObj2,response.context['obj'])
        self.assertTemplateUsed("updateAssoDetails.html")