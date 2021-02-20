from django.db import models
from django.contrib.auth.models import User
from centers.models import Center, CenterReview

# Create your models here.

class Search(models.Model):
    search_query = models.TextField()
    searched_at = models.DateTimeField()
    # search_users = models.ManyToManyField(User, through = 'SearchCount', related_name='search_centers', null = True)

    def __str__(self):
        return f'{self.search_query}'

#class SearchCount(models.Model) :
    #center = models.ForeignKey(Center, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True, null = True)
