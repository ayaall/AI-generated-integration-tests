def test_show_medication_list(self):
    """Test the show_medication_list view"""
    request = self.factory.get('/')
    response = show_medication_list(request)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'show_medication_list.html')
    self.assertEqual(response.context['medication'], [])
