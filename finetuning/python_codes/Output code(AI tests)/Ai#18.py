import pytest

from django.test import TestCase
from.models import Post, PostReport

def createReportPost(request, pk):
    try:
        p = Post.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'error_page.html', {})
    if PostReport.objects.filter(post_id=pk, user_id=request.user.id).exists():
        return render(request, 'error_page.html', {})
    form = reportPostForm()
    user_obj = request.user
    if request.method == 'POST':
        form = reportPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = p
            p.reports_counter = p.reports_counter + 1
            p.save()
            instance.save()
        return redirect('index')

    context = {'form': form, 'user_obj': user_obj, 'post_obj': p}
    return render(request, 'postReportPage.html', context)

def test_create_report_post(request):
    Post.objects.create(title='Test title', content='Test content')
    PostReport.objects.create(post_id=1, user_id=1)
    assert PostReport.objects.filter(post_id=1, user_id=1).exists()
