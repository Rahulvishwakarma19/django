from django.contrib import admin
from users.models import Profile
from users.models import CusOrders, CusRatingFeedback

# Register your models here.

admin.site.register(Profile)
admin.site.register(CusOrders)
admin.site.register(CusRatingFeedback)
