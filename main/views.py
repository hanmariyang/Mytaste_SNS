from django.shortcuts import render, redirect
from content.models import FeedModel

# Create your views here.

def MainHome(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_feed = FeedModel.objects.all().order_by('-created_at')
            return render(request, 'main/home.html', {'feeds': all_feed})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')
