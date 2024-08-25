def afterlogin_view(request):
    """after login for users """
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_staff:
                    auth.login(request, user)
                    return redirect('admin-dashboard')
                if user is not None and user.groups.filter(name='NURSE').exists():
                    auth.login(request, user)
                    return redirect('nurse-dashboard')
                if user is not None and user.groups.filter(name='PATIENT').exists():
                    print("asdasdas")
                    auth.login(request, user)
                    return redirect('patient-dashboard')
                return None
            else:
                messages.info(request, 'invalid username or password')
                return redirect('login')
        else:
            return render(request, 'loginPage.html')
    else:
        if request.user.is_staff:
            return redirect('admin-dashboard')
        if request.user.groups.filter(name='NURSE'):
            return redirect('nurse-dashboard')
        if request.user.groups.filter(name='PATIENT'):
            return redirect('patient-dashboard')
    return None
