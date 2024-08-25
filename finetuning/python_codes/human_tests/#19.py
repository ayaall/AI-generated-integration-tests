def test_sendFeedback(self):
        #if the user is not helpo or manager he cannot send feedback
        self.client.login(username="username",password="password")
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("erro_page.html")
        
        #connect to helpo user 
        self.client.login(username="username2",password="password2")

        #GET
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("sendFeedback.html")       

        #POST 
        response = self.client.post(self.sendFeedback_url,data = {'subject':'subj','content':'conthelpo'},follow=True)  
        self.assertEqual(200,response.status_code)
        f = Feedback.objects.filter(content='conthelpo').first()
        self.assertIsNotNone(f)
        self.assertTemplateUsed("sendFeedback.html") 

        #connect to helpo asso manager 
        self.client.login(username="username3",password="password3")

        #GET
        response = self.client.get(self.sendFeedback_url,follow=True)  
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed("sendFeedback.html")       

        # #POST 
        response = self.client.post(self.sendFeedback_url,data = {'subject':'subj','content':'contmanager'},follow=True)  
        self.assertEqual(200,response.status_code)
        f = Feedback.objects.filter(content='contmanager').first()
        self.assertIsNotNone(f)
        self.assertTemplateUsed("sendFeedback.html")