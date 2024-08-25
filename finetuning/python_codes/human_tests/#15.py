 def test_createPost(self):
        #if user not logged in, he can't create a post
        #check GET
        response = self.client.get(self.createPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("login.html")

        #check POST
        response = self.client.post(self.createPost_url,data ={'info':'postdbchek1','city':'BS','is_asking':True,'category':self.category},follow=True)
        self.assertEqual(200,response.status_code)
        p = Post.objects.filter(info='postdbchek1').first()
        self.assertIsNone(p)    #object didnot exists!

        #preform login to a user
        self.client.login(username="username",password="password")

        #create post
        #check GET
        response = self.client.get(self.createPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.user1,response.context['user_obj'])
        self.assertTrue(response.context['user_obj'].is_authenticated)
        self.assertTemplateUsed("createPostForm.html")
        
        #check POST
        self.client.post(self.createPost_url)
        self.assertTemplateUsed("createPostForm.html")
        response = self.client.post(self.createPost_url,data ={'info':'postdbchek1','city':'BS','is_asking':True,'category':self.category.id}, follow=True)
        p = Post.objects.filter(info='postdbchek1').first()
        self.assertIsNotNone(p)    #object exists after user is authenticated!