def show_medication_list(request):
    """patient show medication list that doctor adds"""
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        user_info = models.Patient.objects.get(user=request.user)
        medication = models.Medication.objects.filter(patient_id=user_info.user_id)
        context = {'medication': medication}
    return render(request, 'show_medication_list.html', context)