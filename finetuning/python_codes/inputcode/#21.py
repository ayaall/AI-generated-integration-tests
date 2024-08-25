def deletePhoto(request,asso_pk,photo_pk):
    asso_obj = Association.objects.get(id=asso_pk)
    if request.user != asso_obj.manager.user and not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"error_page.html",{})

    try:
        photo = Image.objects.get(id=photo_pk)
    except ObjectDoesNotExist:
        return render(request,"admin_error.html",{})

    photo.delete()
    return redirect('associationPhotos',pk=asso_obj.id)