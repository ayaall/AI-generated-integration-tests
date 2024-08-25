def update_kidney_function(request, id_):
    """nurse update Kidney Function """
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id_)
        user.Kidney_function = request.POST['KidneyFunction']
        user.save()
    return render(request, 'updateKidneyFunction.html')
