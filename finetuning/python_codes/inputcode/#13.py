def update_urine_surgery(request, id_):
    """nurse update Urine Surgery """
    if request.method == 'POST':
        user = models.Patient.objects.get(user_id=id_)
        user.Urine_surgery = request.POST['UrineSurgery']
        user.save()
    return render(request, 'updateUrineSurgery.html')