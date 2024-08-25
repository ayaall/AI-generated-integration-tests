@login_required
def createPost(request):
    form = createPostForm()
    user_obj=request.user
    if request.method=='POST':
        form = createPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user_obj.helpouser
            instance.date = datetime.datetime.now()
            instance.save()
        return redirect('showAllPosts')

    context={'form':form,'user_obj':user_obj}
    return render(request, 'createPostForm.html', context)