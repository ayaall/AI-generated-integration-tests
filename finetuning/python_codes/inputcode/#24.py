def categories(request):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    form = Categoryform()
    if request.method=='POST':
        form = Categoryform(request.POST)

        if form.is_valid():
            form.save()
            form = Categoryform()
            return redirect('categories')

    context={
        'form':form,
        'objects':Category.objects.all()
    }
    return render(request, 'categoryFormPage.html',context)
