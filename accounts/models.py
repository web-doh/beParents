from django.db import models
from django.contrib.auth.models import User # User Module를 사용하기 위함

# Create your models here.
class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_realname = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=11)
    user_joindate = models.DateTimeField(auto_now_add=True)
    user_agree_location = models.DateTimeField(null = True)
    user_agree_sms = models.DateTimeField(null = True)    
    # agree 관련 필드 확정 필요

    def __str__(self): # 노출 정보 확정 필요, 우선은 이름만
        if self.user:
            return f'{self.user.get_username()} : {self.user_realname} : {self.user_phone}:{self.user_joindate} : {self.user_agree_location} : {self.user_agree_sms}'
        else:
            return None


 

