def logout_user(request):
    """logout for users """
    logout(request)
    return redirect('login')
def book_appointment(request):
    """patient Book Appointment """
    if request.method == 'POST':
        appointment = models.Appointment()
        appointment.date = request.POST['appointment']
        appointment.time = request.POST['time']
        appointment.name = request.user.username
        appointment.patient_id = request.user.id
        flag = True
        for i in models.Appointment.objects.all():
            if (str(i.date) == str(appointment.date) and
                    str(i.time)[0:5] == str(appointment.time)[0:5]):
                flag = False
                messages.error(request, "The role is already booked")
        if flag:
            appointment.save()
            messages.success(request, "Book Success")
    return render(request, 'BookAppointment.html')