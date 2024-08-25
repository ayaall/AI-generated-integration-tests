def update_blood_pressure(request, id_):
    """nurse update Blood Pressure """
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id_)
        user.Blood_Pressure = request.POST['BloodPressure']
        user.save()
    return render(request, 'updateBloodPressure.html')


@user_passes_test(is_patient)
def update_blood_pressure_patient(request, id_):
    """patient update Blood Pressure """
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id_)
        user.Blood_Pressure = request.POST['BloodPressure']
        user.save()
    return render(request, 'updateBloodPressurePatient.html')