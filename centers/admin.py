from django.contrib import admin
from .models import Center
from .models import CenterReview
from .models import CenterLike


admin.site.register(Center)
admin.site.register(CenterReview)
admin.site.register(CenterLike)


