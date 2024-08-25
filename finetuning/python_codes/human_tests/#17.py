def test_editPost(self):
        #set the url with param of HelpoUserObj id
        self.editPost_url = reverse('editPost', kwargs={'pk':self.post.id})

        #check GET
        response = self.client.get(self.editPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")

        #check POST
        response = self.client.post(self.editPost_url,data ={'info':'i am writing a new post!','city':'BS','is_asking':False,'category':self.category},follow=True)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        p = Post.objects.filter(info='i am writing a new post!').first()
        self.assertNotEqual('BS',p.city)    #object changed his attribute

        #preform login to a user
        self.client.login(username="username",password="password")

        #create post
        #check GET - Get the correct page only if logged in to the correct user
        response = self.client.get(self.editPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.user1,response.context['obj'].user)
        self.assertTrue(response.context['obj'].user.is_authenticated)
        self.assertTemplateUsed("editPost.html")
        
        #check POST - update FORM
        response = self.client.post(self.editPost_url,data ={'info':'i am writing a new post!','city':'BS','is_asking':False,'category':self.category.id}, follow=True)
        self.assertTemplateUsed("editPost.html")
        p = Post.objects.filter(info='i am writing a new post!').first()
        self.assertEqual('BS',p.city)    #object changed his attribute