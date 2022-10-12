# user/views.py
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html')
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        nickname = request.POST.get('nickname', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        profile_image = "basic_profile.png"

        if password != password2:
            return render(request, 'accounts/sign_up.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if email == '' or password == '':
                return render(request, 'accounts/sign_up.html', {'error': '이메일과 패스워드를 입력해주세요.'})
            
            exist_email = get_user_model().objects.filter(email=email)
            exist_nickname = get_user_model().objects.filter(nickname=nickname)
            if exist_email:
                return render(request, 'accounts/sign_up.html', {'error': '이미 존재하는 이메일입니다.'})
            elif exist_nickname:
                return render(request, 'accounts/sign_up.html', {'error': '이미 존재하는 닉네임입니다.'})
            else:
                UserModel.objects.create_user(email=email, username=username, password=password, nickname=nickname, profile_image=profile_image)
                return redirect('/sign-in') # 회원가입이 완료되었으므로 로그인 페이지로 이동



def sign_in_view(request): #로그인
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/sign_in.html')

    elif request.method == 'POST':
        id_nickname_or_email = request.POST.get('id_nickname_or_email', '')
        password = request.POST.get('password', '')
        print(id_nickname_or_email)

        user_email = auth.authenticate(request, email=id_nickname_or_email, password=password) # 사용자 이메일로 불러오기
        user_nickname = auth.authenticate(request, nickname=id_nickname_or_email, password=password) # 사용자 닉네임으로 불러오기
        if user_email is not None:  # 이메일로 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, user_email)
            print("이메일 로그인 성공!")
            return redirect('/')            
        elif user_nickname is not None:  # 닉네임으로 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, user_nickname)
            print("사용자 이름 로그인 성공!")
            return redirect('/')
        else:
            print("로그인 실패")
            return render(request,'accounts/sign_in.html',{'error':'이메일 혹은 패스워드를 확인 해 주세요'})  # 로그인 실패


