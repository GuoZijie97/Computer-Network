from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import goods
from django.contrib import auth
import random

def index(request):
    context = {}
    return render(request, 'sell/index.html', context)

def good(request):
    if request.method == 'POST':
            bname = request.POST['bkname']
            bprice = request.POST['bkprice']
            btype = request.POST['bktype']
            bdescription = request.POST['bkdescription']
            bimage1 = request.FILES['bkimage1']
            bimage2 = request.FILES['bkimage2']
            bimage3 = request.FILES['bkimage3']
            bpk = 1
            if int(btype) <= 4:
                bpk = 1
            elif int(btype) <= 8:
                bpk = 2
            elif int(bype) <= 14:
                bpk = 3
            else:
                bpk = 4
            t = goods.objects.create(goods_id=random.randint(1, 100000), goods_name=bname, goods_category=bpk,
                                    goods_subcategory=btype, goods_info
                                    =bdescription, goods_picture1=bimage1,goods_picture2=bimage2,goods_picture3
                                    =bimage3, goods_price=bprice)
            t.goods_picture1.name = 'upload/' + bimage1.name
            t.goods_picture2.name = 'upload/' + bimage2.name
            t.goods_picture3.name = 'upload/' + bimage3.name
            t.save()
            return render(request, 'sell/upload.html', {'msg': "上传成功！"})

    else:
        somegoods = goods.objects.all()
        return render(request, 'sell/good.html', {'somegoods': somegoods})

def upload(request):
    return render(request, 'sell/upload.html')
