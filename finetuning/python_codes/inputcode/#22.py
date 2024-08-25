def editAssociation(request,pk):
    asso_obj = Association.objects.get(id=pk)
    if request.user != asso_obj.manager.user and not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"error_page.html",{})

    if request.method == 'POST':
        form = associationUpdateForm(request.POST, instance=asso_obj)
        if form.is_valid():
            form.save()
            return redirect('profile',pk=asso_obj.id)
    else:
        form=associationUpdateForm(instance=asso_obj)

    context = {
                'form' : form,
                'obj':asso_obj,
            }

    return render(request,"updateAssoDetails.html",context)