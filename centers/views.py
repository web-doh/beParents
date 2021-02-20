import os
from django.shortcuts import render, redirect
from .models import Center, CenterReview, CenterLike
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponseRedirect

# Create your views here.
#센터 상세페이지
def index(request, center_id):
    center = Center.objects.get(id=center_id)
    reviews = CenterReview.objects.filter(center = center).order_by('-created_at')
    avg_score = CenterReview.objects.values('center').annotate(Avg('score')).filter(center=center)
    NAVER_KEY = os.environ['NAVER_KEY']

    context = {
        'reviews': reviews,
        'center' : center,
        'avg_score' : avg_score,
        'naver_key' : NAVER_KEY 
    }

    return render(request, 'centers/index.html', context)


#리뷰 작성하기
@login_required
def reviews(request, center_id):
    center = Center.objects.get(id=center_id)
    context = {'center': center }

    return render(request, 'centers/reviews.html', context)


#리뷰 저장
@login_required
def save(request, center_id):
    center = Center.objects.get(id=center_id)

    user = request.user
    content = request.POST['content']
    score = request.POST['score']

    image = None
    if 'image' in request.FILES:
        image = request.FILES['image']

    review = CenterReview(user=user, center=center, content=content, score = score, image=image, created_at=timezone.now())
    review.save()

    return redirect('centers:index', center_id = center.id)


#리뷰 수정하기
@login_required
def edit(request, center_id, review_id):
    try:
        center = Center.objects.get(id=center_id)
        review = CenterReview.objects.get(id=review_id, user=request.user)
        next = request.GET.get('next', '')
    except CenterReview.DoesNotExist:
        return redirect('centers:index', center_id = center.id)

    context = {
        'review': review,
        'center' : center,
        'next' : next,
        }
    return render(request, 'centers/edit.html', context)


#리뷰 수정한거 업데이트
@login_required
def update(request, center_id, review_id):
    try:
        review = CenterReview.objects.get(id=review_id, center=center_id, user=request.user)
    except CenterReview.DoesNotExist:
        return redirect('centers:index', center_id = review.center.id)

    review.content = request.POST['content']
    review.score = request.POST['score']
    delete_image = request.POST.get('image__delete', '')
    next=request.POST['next']

    if delete_image == 'delete':
        review.image.delete()

    if 'image' in request.FILES:
        review.image = request.FILES['image']

    review.save()

    return redirect(next)

#리뷰 삭제

def delete(request, center_id, review_id):
    try:
        center = Center.objects.get(id=center_id)
        review = CenterReview.objects.get(id=review_id, user=request.user)
    except CenterReview.DoesNotExist:
        return redirect('centers:index', center_id = center.id)

    review.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#센터 찜

def like(request, center_id):

    if request.method == 'POST':
        
        try:
            center = Center.objects.get(id=center_id)
            center_like = CenterLike.objects.all()

            if request.user in center.like_users.all():
                center.like_users.remove(request.user)

            else:
                center.like_users.add(request.user)
                user = request.user
                user.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


        except Center.DoesNotExist:
            pass
        
    return redirect('centers:index', center_id = center.id)