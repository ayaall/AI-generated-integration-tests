def editPost(request, pk):
    post = Post.objects.get(id=pk)

    user_obj = HelpoUser.objects.get(user = post.user)
    if request.user != user_obj.user:
        return render(request,"error_page.html",{})

    if request.method == 'POST':
        form = createPostForm(request.POST, instance=post)

        if form.is_valid():
            updatePostDate(post)
            form.save()
            return redirect('showMyPosts',pk = user_obj.user_id)

    else:
        form = createPostForm(instance=post)
    context = {
                'form' : form,
                'obj':user_obj,
            }
    return render(request,"editPost.html",context)
