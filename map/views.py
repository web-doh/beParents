import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Center, CenterReview
from haversine import haversine
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count


# Create your views here.
def index(request):
    NAVER_KEY = os.environ['NAVER_KEY']
    context = {'naver_key' : NAVER_KEY }

    return render(request, 'map/index.html', context)


#X=위도, Y=경도

@csrf_exempt
def ajax(request):
    if 'userX' in request.POST:
        userX = request.POST['userX']
    if 'userY' in request.POST:
        userY = request.POST['userY']
    if 'mapX' in request.POST:
        mapX = request.POST['mapX']
    if 'mapY' in request.POST:
        mapY = request.POST['mapY']
    
    user_location = {float(userX), float(userY)} # 현재 위치 받아오기

    # centers = Center.objects.all()

    near_centers_list = [] # 센터이름 & 현재위치와 센터간 거리

    x_threshold = 0.02 #위도 기준 2km 이내 (양방으로는 4km)
    y_threshold = 0.03 #경도 기준 2km 이내 (양방으로는 3km)

    centers = Center.objects.filter(
        x__gt=float(mapX) - x_threshold, 
        x__lt=float(mapX) + x_threshold, 
        y__gt=float(mapY) - y_threshold, 
        y__lt=float(mapY) + y_threshold
    )


    for center in centers :
        center_location = (center.x, center.y) 
        user_distance = haversine(user_location, center_location, unit= 'km') # 거리 구하기(km 기준, unit으로 기준 변경 가능)
        avg_score = CenterReview.objects.values('center').annotate(Avg('score'), Count('score')).filter(center=center)

        center = {
            'id': center.id ,
            'name' : center.center_name,
            'address' : center.center_address,
            'x' : center.x,
            'y' : center.y,
            'distance' : round(user_distance, 3),
            'type' : center.center_type,
            'score' : avg_score,
            'review' : avg_score
        }
        near_centers_list.append(center)

#        if len(near_centers_list) < 1:
#            for center in centers :
#                center_location = (center.x, center.y) 
#                user_distance = haversine(user_location, center_location, unit= 'km') # 거리 구하기(km 기준, unit으로 기준 변경 가능)
#                avg_score = CenterReview.objects.values('center').annotate(Avg('score'), Count('score')).filter(center=center)
    
#                    center = {
#                        'id': center.id ,
#                        'name' : center.center_name,
#                        'address' : center.center_address,
#                        'x' : center.x,
#                        'y' : center.y,
#                        'distance' : round(user_distance, 3),
#                        'type' : center.center_type,
#                        'score' : avg_score,
#                        'review' : avg_score,
                        #'review' : review_dict[center.center_name],
                        #'score' : score_dict[center.center_name]
#                    }
#                    near_centers_list.append(center)
        
    near_centers_list.sort(key=(lambda x: x['distance'])) # 사용자 거리순 정렬
    
    context = { 
                'near_centers_list' : near_centers_list
            }

    return render(request, 'map/center_summary.html', context)

    




