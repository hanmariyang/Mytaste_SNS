from django.shortcuts import render, redirect
from content.models import FeedModel




# Create your views here.

def UploadFeed(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            return render(request, 'content/upload_feed.html')
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        # image = "https://i1.ruliweb.com/img/22/10/04/1839e60028750ad5d.jpg"
        # content = request.data.get('content')
        # created_at = request.data.get('created_at')
        # updated_at = request.data.get('updated_at')
        # profile_image = "basic_profile.png"

        # feed = feed.objects.create(image=image, content=content, profile_image=profile_image, like_count=0, created_at=created_at, updated_at=updated_at)

        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_feed = FeedModel()  # 글쓰기 모델 가져오기
        my_feed.author = user  # 모델에 사용자 저장
        my_feed.content = request.POST.get('content', '')  # 모델에 글 저장
        my_feed.like_count = 0
        my_feed.image = "https://i1.ruliweb.com/img/22/10/04/1839e60028750ad5d.jpg"
        my_feed.save()
        return render(request, 'main/home.html')