def update_glucose(request, id_):
    """nurse update Glucose """
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id_)
        user.Glucose = request.POST['Glucose']
        user.save()
    return render(request, 'updateGlucose.html')
