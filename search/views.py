from django.shortcuts import render, redirect
from .models import Search
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView
from .models import Center, CenterReview
from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from haversine import haversine
from collections import Counter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):

    hashtags = Center.objects.values('hashtags')

    hashtag_list = [] # 전체 hashtag 리스트를 만든다

    for hashtag in hashtags :
        values = hashtag['hashtags']
        for value in values :
            hashtag_list.append(value)
    
    hashtag_count = Counter(hashtag_list) # hashtag couter 딕셔너리를 만든다. ex) {'아동발달' : 5, '미술치료' : 2} / 갯수많은 순서대로 자동 sorting
    top10_dict = dict(Counter(hashtag_count).most_common(10))
    hashtag_top10 = list(top10_dict.keys())
    
    
    context = {
        'hashtag_top10' : hashtag_top10
        }
    
    return render(request, 'search/index.html', context)


def center_list(request):
    
    try:
        userX = request.GET['userX']
        userY = request.GET['userY']
        user_location = (float(userX), float(userY))
    except:
        user_location = (37.5666103, 126.9783882)

    centers = None
    query = None
    if 'query' in request.GET:
        query = request.GET.get('query')
        all_centers = Center.objects.all().filter(Q (center_name__icontains=query) | Q (center_type__icontains=query) | Q (hashtags__icontains=query))
  
        center_list = []

        for center in all_centers:
            center_location = (center.x, center.y) 
            user_distance = haversine(user_location, center_location, unit= 'km')
            reviews = CenterReview.objects.values('center').annotate(Avg('score'), Count('score')).filter(center=center)


            center = {
                'id': center.id ,
                'name' : center.center_name,
                'address' : center.center_address,
                'x' : center.x,
                'y' : center.y,
                'distance' : round(user_distance, 3),
                'type' : center.center_type,
                'review' : reviews
            }
            center_list.append(center)

        center_list.sort(key=(lambda x: x['distance'])) # 사용자 거리순 정렬

        paginator = Paginator(center_list, 10)
        page = request.GET.get('page')


        try:
            centers = paginator.page(page)
        except PageNotAnInteger:
            centers = paginator.page(1)
        except EmptyPage:
            centers = paginator.page(paginator.num_pages)




    
    context = { 
                'centers' : centers,
                'query' : query,
                'userX' : userX,
                'userY' : userY,
    
            }
    

    return render(request, 'search/center_list.html', context)



def center_list_ajax(request):
    try:
        userX = request.GET['userX']
        userY = request.GET['userY']
        user_location = (float(userX), float(userY))
    except:
        user_location = (37.5666103, 126.9783882)


    centers = None
    query = None
    if 'query' in request.GET:
        query = request.GET.get('query')
        all_centers = Center.objects.all().filter(
            Q (center_name__icontains=query) | Q (center_type__icontains=query) | Q (hashtags__icontains=query)
        )



        center_list = []

        for center in all_centers:
            center_location = (center.x, center.y) 
            user_distance = haversine(user_location, center_location, unit= 'km')
            reviews = CenterReview.objects.values('center').annotate(Avg('score'), Count('score')).filter(center=center)


            center = {
                'id': center.id ,
                'name' : center.center_name,
                'address' : center.center_address,
                'x' : center.x,
                'y' : center.y,
                'distance' : round(user_distance, 3),
                'type' : center.center_type,
                'review' : reviews
            }
            center_list.append(center)

        center_list.sort(key=(lambda x: x['distance'])) # 사용자 거리순 정렬


        paginator = Paginator(center_list, 10)
        page = request.GET.get('page')

        


        try:
            centers = paginator.page(page)
        except PageNotAnInteger:
            centers = paginator.page(1)
        except EmptyPage:
            centers = None
            



    
    context = { 
                'centers' : centers,
                'query' : query,

            }
    

    return render(request, 'search/center_list_ajax.html', context)



