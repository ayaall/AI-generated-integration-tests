def admin_book_appointment(request):
    """admin book appointment for the patient """
    patient = models.Patient()
    if request.method == 'POST':
        check = False
        for i in models.Patient.objects.all():
            if i.user.username == request.POST['patientName']:
                check = True
                patient = i
        if check:
            appointment = models.Appointment()
            appointment.date = request.POST['appointment']
            appointment.time = request.POST['time']
            appointment.name = patient.user
            appointment.patient_id = patient.user_id
            flag = True
            for i in models.Appointment.objects.all():
                if (str(i.date) == str(appointment.date)
                        and str(i.time)[0:5] == str(appointment.time)):
                    flag = False
                    messages.error(request, "The role is already booked")
            if flag:
                appointment.save()

                messages.success(request, "Book Success")
    return render(request, 'AdminBookAppointment.html', {'patients': models.Patient.objects.all()})