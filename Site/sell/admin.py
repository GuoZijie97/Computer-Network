from django.contrib import admin

# Register your models here.
from .models import user, goods, order

admin.site.register(user)
admin.site.register(goods)
admin.site.register(order)
