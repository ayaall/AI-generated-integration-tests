@user_passes_test(is_nurse)
def nurse_view_food(request):
    """nurse show food list """
    food = models.Food.objects.all()
    dict = {}
    dict['user'] = models.Nurse.objects.get(user_id=request.user.id)
    dict['food'] = food
    return render(request, 'nurse_view_food.html', context=dict)
@user_passes_test(is_nurse)
def nurse_add_food(request):
    """nurse add food to list """
    flag = False
    dict = {}
    dict['user'] = models.Nurse.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        food = models.Food()
        for i in models.Food.objects.all():
            if i.Name == request.POST['Name']:
                flag = True

        food.Name = request.POST['Name']
        food.number = request.POST['num']
        food.max_Cholesterol = request.POST['max_Cholesterol']
        food.max_Liver_function = request.POST['max_Liver_function']
        food.max_Kidney_function = request.POST['max_Kidney_function']
        food.max_Blood_Pressure = request.POST['max_Blood_Pressure']
        food.pic = request.FILES['pic']
        if flag is False:
            food.save()
        else:
            messages.error(request, "The role is already booked")

        return HttpResponseRedirect('nurse-dashboard')
    return render(request, 'nurse_add_food.html', context=dict)
