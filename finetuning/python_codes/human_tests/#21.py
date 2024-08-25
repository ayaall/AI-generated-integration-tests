 def test_deletePhoto(self):
        response = self.client.get(self.deletePhoto_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        #connect to the asso manager user
        self.client.login(username="username",password="password")
        response = self.client.get(self.deletePhoto_url_error,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        
        self.client.login(username="username",password="password")
        response = self.client.get(self.deletePhoto_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("assoPhotos.html")