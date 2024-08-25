def associationPhotos(request,pk):
    asso_obj = Association.objects.get(id=pk)
    photos = Image.objects.filter(asso=pk)
    if request.user != asso_obj.manager.user and not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"error_page.html",{})

    if request.method == 'POST':
        i_form = ImageFrom(request.POST,files=request.FILES)
        if i_form.is_valid():
            instance = i_form.save(commit=False)
            instance.asso = asso_obj
            instance.save()
            return redirect('associationPhotos',pk=asso_obj.id)
    else:
        i_form = ImageFrom()

    context = {
                'i_form': i_form,
                'obj':asso_obj,
                'photos':photos
            }

    return render(request,"assoPhotos.html",context)
