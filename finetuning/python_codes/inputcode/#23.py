def editCategory(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})

    c = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = Categoryform(request.POST, instance=c)

        if form.is_valid():
            form.save()
            return redirect('categories')

    else:
        form=Categoryform(instance=c)

    context = {
                'form' : form,
                'obj':c,
            }

    return render(request, 'editCategory.html', context)
