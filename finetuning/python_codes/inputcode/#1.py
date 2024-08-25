def is_nurse(user):
    """check if user in nurse """
    return user.groups.filter(name='NURSE').exists()
	
def nurse_dashboard(request):
    """nurse dashboard """
    mydict = {
    }
    return render(request, 'nurse_dashboard.html', context=mydict)
