from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Center, CenterLike, CenterReview, Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

    context = {
        'profile' : profile
    }
    return render(request, 'mypage/index.html', context)

@login_required
def mylikes(request):
    likes = CenterLike.objects.filter(user=request.user)
    
    context = {
        'likes' : likes

    }
    return render(request, 'mypage/mylikes.html', context)

@login_required
def myreviews(request):
    reviews = CenterReview.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'reviews':reviews

    }
    return render(request, 'mypage/myreviews.html', context)

@login_required
def myinfo(request):
    return render(request, 'mypage/myinfo.html')

    