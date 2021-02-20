from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import os
from django.conf import settings

class Center(models.Model):
    n_id = models.IntegerField(null=True)
    center_name = models.CharField(max_length=100, null=True)
    center_type = models.CharField(max_length=100, null=True)
    center_phone = models.CharField(max_length=100, null=True)
    center_address = models.CharField(max_length=100, null = True)
    homepage = models.CharField(max_length=200, null=True)
    runhours = models.CharField(max_length=200, null=True)
    hashtags = models.JSONField(default=list, null=True)

    content_urls = models.JSONField(default=list, null=True)
    contents = models.JSONField(default=list, null=True)
    x = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    y = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    like_users = models.ManyToManyField(User, through = 'CenterLike', related_name='like_centers', null = True)
    review_users = models.ManyToManyField(User,through='CenterReview', related_name='review_centers', null = True)


    def __str__(self):
            return f'{self.id}: {self.center_name} : {self.center_type} : {self.center_phone} : {self.center_address} :{self.homepage} : {self.runhours} : {self.hashtags} : {self.content_urls} : {self.contents} : {self.x} : {self.y}'


class CenterReview(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.TextField(null = True)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null = True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    image = models.ImageField(blank=True, null=True, upload_to='centers')
    
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        super(CenterReview, self).delete(*args, **kargs)

    def __str__(self):

        if self.user:
            return f' {self.user.get_username()} : {self.center.center_name} : {self.score} : {self.content}'
            
        return f'{self.score} : {self.content}'



class CenterLike(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):

        if self.user:
            return f'{self.user.get_username()} : {self.center.center_name} : {self.created_at}'
            
        return None








    