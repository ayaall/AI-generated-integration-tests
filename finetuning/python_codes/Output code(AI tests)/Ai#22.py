@tag("editAssociation")
def test_edit_association(self):
    """Test the edit_association function."""
    # Create a user
    user = self._create_user("test@example.com", "test")

    # Create an association
    association = self._create_association(user)

    # Create a request
    request = self._create_request(association)

    # Call the function
    response = self._edit_association(request, association.id)

    # Check the response status code
    self.assertEqual(response.status_code, 200)

    # Check the form instance
    form = response.context['form']
    self.assertEqual(form.instance.id, association.id)

    # Check the template used
    template = response.template
    self.assertEqual(template.name, 'updateAssoDetails.html')

    # Check the context
    context = response.context
    self.assertEqual(context['obj'].id, association.id)
