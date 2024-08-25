def test_showMyPosts(self):
        #set the url with param of HelpoUserObj id
        self.showMyPosts_url = reverse('showMyPosts', kwargs={'pk':self.HelpoUserObj.user.id})

        #if the user requested the site page is not the user id in url param
        response = self.client.get(self.showMyPosts_url)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("error_page.html")
        
        # Check error page
        self.client.login(username="username",password="password")
        response = self.client.get(self.showMyPosts_url)

        #check if the data that send is the correct data
        self.assertEqual(200,response.status_code)
        self.assertEqual(self.HelpoUserObj.user.id,response.context['user'].id)
        posts = Post.objects.filter(user_id=self.HelpoUserObj.user.id)
        self.assertEqual(list(posts),list(response.context['posts']))
        self.assertTemplateUsed("myPosts.html")