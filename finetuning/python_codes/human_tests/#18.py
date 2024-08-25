def test_createReportPost_with_login(self):
        #create post instance
        #without login will send him to login page
        response = self.client.get(self.createReportPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("login.html")

        #login to user
        self.client.login(username="username",password="password")

        #error page  -  post not found
        response = self.client.get(self.createReportPost_postError_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        
        #creating a new post
        self.client.post(self.createPost_url)
        self.assertTemplateUsed("createPostForm.html")
        response = self.client.post(self.createPost_url,data ={'info':'postreport','city':'BS','is_asking':True,'category':self.category.id}, follow=True)
        p = Post.objects.filter(info='postreport').first()
        self.assertIsNotNone(p)    #object exists after user is authenticated!

        self.createReportPost_url = reverse('createReportPost', kwargs={'pk':p.id})

        #post found
        #GET the page
        response = self.client.get(self.createReportPost_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("postReportPage.html")
        
        #POST - creating a new report 
        self.client.post(self.createReportPost_url,{'info':'abc'})
        pr = PostReport.objects.filter(info='abc')
        self.assertIsNotNone(pr)
        self.assertTemplateUsed("index.html")

        #Try to report again on the same post will now be allowed
        self.client.post(self.createReportPost_url,{'info':'abcd'})
        pr = PostReport.objects.filter(info='abcd')
        self.assertEqual([],list(pr))
        self.assertTemplateUsed("error_page.html")