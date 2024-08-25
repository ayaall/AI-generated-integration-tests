def nurse_add_record(request, id_nurse):
    """nurse add record """
    dict = {}
    dict['patients'] = models.Patient.objects.all()
    dict['user'] = models.Nurse.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        record = models.Record()
        record.patientName = request.POST['patientName']
        record.body = request.POST['body']
        record.nurse_id = id_nurse
        record.save()
        return render(request, 'nurse_Record.html')
    return render(request, 'nurse_Record.html', context=dict)