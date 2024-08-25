def patient_dashboard(request):
    """patient dashboard """
    mydict = {}
    user = models.Patient.objects.get(user_id=request.user.id)
    # for i in models.Patient.objects.all():
    #     if i.user.id == user.id:
    mydict['user'] = user
    return render(request, 'patient_dashboard.html', context=mydict)
