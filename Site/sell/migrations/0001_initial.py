# Generated by Django 2.1.2 on 2018-10-30 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=30)),
                ('goods_category', models.CharField(choices=[('1', '生活用品'), ('2', '图书文具'), ('3', '鞋服配饰'), ('4', '其他')], max_length=5)),
                ('goods_subcategory', models.CharField(choices=[('1', '家具'), ('2', '家纺'), ('3', '其他'), ('4', '文具'), ('5', '教材教辅'), ('6', '课外书'), ('7', '男装'), ('8', '女装'), ('9', '配饰'), ('10', '箱包'), ('11', '化妆品'), ('12', '数码'), ('13', '娱乐休闲'), ('14', '运动')], max_length=6)),
                ('goods_picture', models.ImageField(upload_to='./sell/')),
                ('goods_price', models.FloatField(max_length=15)),
                ('goods_info', models.CharField(max_length=400)),
                ('goods_other_info', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('orderNo', models.AutoField(primary_key=True, serialize=False)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_sell_id', to='sell.goods', verbose_name="the seller's id")),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=18)),
                ('user_name', models.CharField(max_length=18)),
                ('user_email', models.CharField(max_length=30)),
                ('user_phone', models.IntegerField(default=0)),
                ('user_rating', models.FloatField(max_length=18)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_buyer_id', to='sell.user', verbose_name="the buyer's id"),
        ),
        migrations.AddField(
            model_name='goods',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sell.user'),
        ),
    ]