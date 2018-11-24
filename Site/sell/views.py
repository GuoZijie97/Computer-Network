from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import goods, order
from PIL import Image
from shesite.settings import MEDIA_ROOT
import time
import os



def index(request):
    goods_list = goods.objects.filter(is_sold=False).order_by('-goods_time')
    first_goods = goods_list.first()
    if first_goods is not None:
        if goods_list.count() > 4:
            goods_list = goods_list[0:3]

    context = {
        'goods_list': goods_list,
        'first_goods': first_goods,
    }

    return render(request, 'sell/index.html', context)

@login_required
def upload(request):
    if request.method == 'POST':
            bname = request.POST['bkname']
            bprice = request.POST['bkprice']
            btype = request.POST['bktype']
            bdescription = request.POST['bkdescription']

            bimage1 = request.FILES['bkimage1']
            pic1_x =float(request.POST['pic1_x'])
            pic1_y = float(request.POST['pic1_y'])
            pic1_height = float(request.POST['pic1_height'])
            pic1_width = float(request.POST['pic1_width'])

            bimage2 = request.FILES['bkimage2']
            pic2_x = float(request.POST['pic2_x'])
            pic2_y = float(request.POST['pic2_y'])
            pic2_height = float(request.POST['pic2_height'])
            pic2_width = float(request.POST['pic2_width'])

            bimage3 = request.FILES['bkimage3']
            pic3_x = float(request.POST['pic3_x'])
            pic3_y = float(request.POST['pic3_y'])
            pic3_height = float(request.POST['pic3_height'])
            pic3_width = float(request.POST['pic3_width'])

            bpk = 1
            if int(btype) <= 4:
                bpk = 1
            elif int(btype) <= 8:
                bpk = 2
            elif int(btype) <= 14:
                bpk = 3
            else:
                bpk = 4

            t = goods.objects.create(goods_name=bname, goods_category=bpk,
                                    goods_subcategory=btype, goods_info
                                    =bdescription, goods_picture1=bimage1,goods_picture2=bimage2,goods_picture3
                                    =bimage3, goods_price=bprice, seller=request.user)
            t.save()

            image1 = Image.open(t.goods_picture1)
            cropped_image1 = image1.crop((pic1_x, pic1_y, pic1_width + pic1_x, pic1_height + pic1_y))
            resized_image1 = cropped_image1.resize((200, 200), Image.ANTIALIAS)
            filename1 = str(t.goods_picture1)
            newimage1 = os.path.join(MEDIA_ROOT, filename1)
            resized_image1.save(newimage1)

            image2 = Image.open(t.goods_picture2)
            cropped_image2 = image2.crop((pic2_x, pic2_y, pic2_width + pic2_x, pic2_height + pic2_y))
            resized_image2 = cropped_image2.resize((200, 200), Image.ANTIALIAS)
            filename2 = str(t.goods_picture2)
            newimage2 = os.path.join(MEDIA_ROOT, filename2)
            resized_image2.save(newimage2)

            image3 = Image.open(t.goods_picture3)
            cropped_image3 = image3.crop((pic3_x, pic3_y, pic3_width + pic3_x, pic3_height + pic3_y))
            resized_image3 = cropped_image3.resize((200, 200), Image.ANTIALIAS)
            filename3 = str(t.goods_picture3)
            newimage3 = os.path.join(MEDIA_ROOT, filename3)
            resized_image3.save(newimage3)

            t.save()

            return render(request, 'sell/upload.html', {'msg': "上传成功！"})

    else:
        return render(request, 'sell/upload.html')


def subcategory_view(request, goods_subcategory):
    if request.method == 'POST':
        order_by_what = request.POST['order_by_what']
        if order_by_what == 'time':
            goods_list = goods.objects.filter(goods_subcategory=goods_subcategory, is_sold=False).order_by(
                '-goods_time')
        elif order_by_what == 'price_asc':
            goods_list = goods.objects.filter(goods_subcategory=goods_subcategory, is_sold=False).order_by(
                'goods_price')
        else:
            goods_list = goods.objects.filter(goods_subcategory=goods_subcategory, is_sold=False).order_by(
                '-goods_price')

        first_goods = goods_list.first()
        num_of_goods = goods_list.count()
        paginator = Paginator(goods_list, 9)
        page = request.GET.get('page')
        one_page_list = paginator.get_page(page)

        if first_goods is not None:
            subcategory_name = first_goods.get_goods_subcategory_display()
            context = {
                'one_page_list': one_page_list,
                'subcategory_name': subcategory_name,
                'first_goods': first_goods,
                'num_of_goods': num_of_goods,
            }
        else:
            context = {
                'one_page_list': one_page_list,
                'first_goods': first_goods,
                'num_of_goods': num_of_goods,
            }

    else:
        order_by_what = request.GET.get('order_by_what')
        if order_by_what == 'price_desc':
            goods_list = goods.objects.filter(goods_subcategory=goods_subcategory, is_sold=False).order_by(
                '-goods_price')
        elif order_by_what == 'price_asc':
            goods_list = goods.objects.filter(goods_subcategory=goods_subcategory, is_sold=False).order_by(
                'goods_price')
        else:
            goods_list = goods.objects.filter(goods_subcategory=goods_subcategory, is_sold=False).order_by(
                '-goods_time')

        first_goods = goods_list.first()
        num_of_goods = goods_list.count()
        paginator = Paginator(goods_list, 9)
        page = request.GET.get('page')
        one_page_list = paginator.get_page(page)

        if first_goods is not None:
            subcategory_name = first_goods.get_goods_subcategory_display()
            context = {
                'one_page_list': one_page_list,
                'subcategory_name': subcategory_name,
                'first_goods': first_goods,
                'num_of_goods': num_of_goods,
            }
        else:
            context = {
                'one_page_list': one_page_list,
                'first_goods': first_goods,
                'num_of_goods': num_of_goods,
            }
    return render(request, 'sell/subcategory_goods_list.html', context)

@login_required
def detail(request, pk):
    good = goods.objects.get(pk=pk)
    user_profile = UserProfile.objects.get(user=good.seller)

    if request.method == 'POST':
        order_start = order.objects.create(goods=good, buyer=request.user)
        order_start.save()

        return render(request, 'sell/index.html')

    else:
        return render(request, 'sell/single-product-details.html', {'good': good,
                                                                    'user_profile': user_profile})


@login_required
def confirm(request):
    if request.method == 'POST':
        id = request.POST['goodsid']
        order.objects.filter(goods__goods_id=id).update(is_done=True)
        goods.objects.filter(goods_id=id).update(is_sold=True)

        orders_list = order.objects.filter(goods__seller=request.user, is_done=False).order_by('-order_time')
        first_goods = orders_list.first()

        paginator = Paginator(orders_list, 9)
        page = request.GET.get('page')
        one_page_list = paginator.get_page(page)

        context = {
                'one_page_list': one_page_list,
                'first_goods': first_goods,
            }

        return render(request, 'sell/confirm.html', context)

    else:
        orders_list = order.objects.filter(goods__seller=request.user, is_done=False).order_by('-order_time')
        first_goods = orders_list.first()

        paginator = Paginator(orders_list, 9)
        page = request.GET.get('page')
        one_page_list = paginator.get_page(page)

        context = {
            'one_page_list': one_page_list,
            'first_goods': first_goods,
        }

        return render(request, 'sell/confirm.html', context)

@login_required
def is_selling(request):
    if request.method == 'POST':
        id = request.POST['goodsid']
        goods.objects.filter(goods_id=id).delete()

        goods_list = goods.objects.filter(seller=request.user, is_sold=False).order_by('-goods_time')
        first_goods = goods_list.first()

        paginator = Paginator(goods_list, 9)
        page = request.GET.get('page')
        one_page_list = paginator.get_page(page)

        context = {
                'one_page_list': one_page_list,
                'first_goods': first_goods,
            }

        return render(request, 'sell/is_selling.html', context)

    else:
        goods_list = goods.objects.filter(seller=request.user, is_sold=False).order_by('-goods_time')
        first_goods = goods_list.first()

        paginator = Paginator(goods_list, 9)
        page = request.GET.get('page')
        one_page_list = paginator.get_page(page)

        context = {
            'one_page_list': one_page_list,
            'first_goods': first_goods,
        }

        return render(request, 'sell/is_selling.html', context)

def graduation(request):
    goods_list = goods.objects.filter(is_sold=False).order_by('-goods_time')
    first_goods = goods_list.first()

    paginator = Paginator(goods_list, 9)
    one_page_list = paginator.get_page(1)

    context = {
        'one_page_list': one_page_list,
        'first_goods': first_goods,
    }

    return render(request, 'sell/graduation.html', context)
