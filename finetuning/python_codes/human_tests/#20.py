 def test_associationPhotos(self):
        response = self.client.get(self.associationPhotos_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        self.client.login(username="username",password="password")
        response = self.client.get(self.associationPhotos_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("assoPhotos.html")

        response = self.client.post(self.associationPhotos_url, data ={'img':tempfile.NamedTemporaryFile(suffix=".jpg")})  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("assoPhotos.html")