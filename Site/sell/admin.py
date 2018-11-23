from django.contrib import admin

# Register your models here.
from .models import goods, order
from users.models import UserProfile

admin.site.register(UserProfile)
admin.site.register(goods)
admin.site.register(order)
