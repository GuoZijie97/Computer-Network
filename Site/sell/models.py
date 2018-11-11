from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_password = models.CharField(max_length=18)
    user_name = models.CharField(max_length=18)
    user_email = models.CharField(max_length=30)
    user_phone = models.IntegerField(default=0)
    user_rating = models.FloatField(max_length=18)

class goods(models.Model):

    Goods_Category = (
        ('1', "生活用品"),
        ('2', "图书文具"),
        ('3', "鞋服配饰"),
        ('4', "其他"),
    )

    Goods_SubCategory = (
        ('1', "家具"),
        ('2', "家纺"),
        ('3', "其他"),
        ('4', "文具"),
        ('5', "教材教辅"),
        ('6', "课外书"),
        ('7', "男装"),
        ('8', "女装"),
        ('9', "配饰"),
        ('10', '箱包'),
        ('11', '化妆品'),
        ('12', '数码'),
        ('13', '娱乐休闲'),
        ('14', '运动'),
    )
    goods_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(user, on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=30)
    goods_category = models.CharField(max_length=5, choices=Goods_Category)
    goods_subcategory = models.CharField(max_length=6, choices=Goods_SubCategory)
    goods_picture = models.ImageField(upload_to='./sell/', height_field=None, width_field=None)
    goods_price = models.FloatField(max_length=15)
    goods_info = models.CharField(max_length=400)
    goods_other_info = models.CharField(max_length=400)

class order(models.Model):
    orderNo = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='order_sell_id', verbose_name="the seller's id",)
    seller_id = models.ForeignKey(user, on_delete=models.CASCADE, related_name='order_buyer_id', verbose_name="the buyer's id",)
