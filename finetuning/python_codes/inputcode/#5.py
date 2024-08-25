def update_ecg(request, id_):
    """nurse update ECG test """
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id_)
        user.ECG = request.POST['ECG']
        user.save()
    return render(request, 'updateECG.html')