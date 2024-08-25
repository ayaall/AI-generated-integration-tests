def test_update_glucose(self):
    """nurse update Glucose """
    self.client.post('/updateGlucose/', {'Glucose': '2'})
    user = models.Patient.objects.get(user_id=self.user.id)
    self.assertEqual(user.Glucose, '2')
