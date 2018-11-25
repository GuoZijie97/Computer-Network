from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class goods(models.Model):

    Goods_Category = (
        ('1', "鞋服配饰"),
        ('2', "生活用品"),
        ('3', "交通工具"),
        ('4', "图书电子"),
    )

    Goods_SubCategory = (
        ('1', "女装"),
        ('2', "男装"),
        ('3', "鞋靴"),
        ('4', "配饰/箱包"),
        ('5', "美妆洗护"),
        ('6', "家具"),
        ('7', "家纺/家饰"),
        ('8', "百货"),
        ('9', "自行车"),
        ('10',"电动车"),
        ('11', "配件"),
        ('12', "图书"),
        ('13', "文具"),
        ('14', "数码/电器"),
    )
    goods_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goods_seller', verbose_name="the good's seller")
    goods_name = models.CharField(max_length=30)
    goods_category = models.CharField(max_length=2, choices=Goods_Category)
    goods_subcategory = models.CharField(max_length=2, choices=Goods_SubCategory)
    goods_picture1 = models.ImageField(upload_to='img_upload/%Y/%m/%d', height_field=None, width_field=None, default='img_upload/default.jpg')
    goods_picture2 = models.ImageField(upload_to='img_upload/%Y/%m/%d', height_field=None, width_field=None, default='img_upload/default.jpg')
    goods_picture3 = models.ImageField(upload_to='img_upload/%Y/%m/%d', height_field=None, width_field=None, default='img_upload/default.jpg')
    goods_price = models.FloatField(max_length=15)
    goods_info = models.CharField(max_length=400)
    goods_time = models.DateTimeField(auto_now=True, auto_now_add=False,)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.goods_name

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    goods = models.OneToOneField(goods, on_delete=models.CASCADE,)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_buyer', verbose_name="the order's buyer",)
    order_time = models.DateTimeField(auto_now=True, auto_now_add=False,)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id

class like(models.Model):
    like_id = models.AutoField(primary_key=True)
    goods = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='goods_liker', verbose_name="the goods liked",)
    liker =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_like', verbose_name="the goods liker",)
    like_time = models.DateTimeField(auto_now=True, auto_now_add=False,)

    def __str__(self):
        return self.like_id