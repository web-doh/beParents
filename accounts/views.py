from django.shortcuts import render, redirect
from django.http import JsonResponse 
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    return render(request, 'accounts/index.html')

@login_required
def complete(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    context = { 'profile': profile } 
    return render(request, 'accounts/complete.html', context)


def sign_up(request):
    context = {}

    #POST Method
    if request.method == 'POST': 
        if(request.POST['username'] and
            request.POST['password'] and
            request.POST['password'] == request.POST['password_check']):
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user_realname = request.POST['user_realname']
            user_phone = request.POST['user_phone']
            user_agree_location = request.POST.get('user_agree_location', '')
            user_agree_sms = request.POST.get('user_agree_sms', '')

            if user_agree_location == 'on':
                user_agree1 = timezone.now()
            else: 
                user_agree1 = None

            if user_agree_sms == 'on':
                user_agree2 = timezone.now()
            else: 
                user_agree2 = None
                
            profile = Profile(user=user, user_realname=user_realname, user_phone=user_phone, user_joindate=timezone.now(), user_agree_location=user_agree1, user_agree_sms=user_agree2 )
            profile.save()

            auth.login(request, user)
            return redirect('accounts:complete', profile_id=profile.id)

        #GET Method
    return render(request, 'accounts/sign_up.html', context)


# 아이디 중복 체크 
def check_id_duplicate(request):
    username = request.GET.get('username')
    try:
        # 중복 검사 실패
        user = User.objects.get(username=username)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        duplicate = "pass"
    else: 
        duplicate = "fail"
    context = { 'duplicate': duplicate }
    return JsonResponse(context)


def login(request):
    context = {}
    
    #POST Method
    if request.method == 'POST':
        next=request.POST['next']
        
        if request.POST['username'] and request.POST['password']:
            user = auth.authenticate(
            request,
                username=request.POST['username'],
                password=request.POST['password'],
                
            )

            if user is not None:
                auth.login(request, user)

                return redirect(next)
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요'

        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요'

    #GET Method
    next = request.GET['next']

    if request.user.is_authenticated:
        return redirect(next)
        
    context['next'] = next
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('mypage:index')

