def test_edit_association(self):
    # Log in as a user
    self.client.login(username='test', password='test')
    
    # Send a GET request to the edit association view
    response = self.client.get(reverse('edit_association', args=[1]))
    # Verify that the status code is 200 (OK)
    self.assertEqual(response.status_code, 200)
    
    # Send a POST request to update the association
    response = self.client.post(reverse('edit_association', args=[1]), {
        'name': 'test',
        'description': 'test',
        'manager': self.user,
        'members': self.user,
    })
    # Verify that the status code is 200 (OK)
    self.assertEqual(response.status_code, 200)
