
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from .models import goods, order


def index(request):
    context = {}
    return render(request, 'sell/index.html', context)

def subcategory_view(request, goods_subcategory):
    goods_list = get_list_or_404(goods, goods_subcategory=goods_subcategory)
    first_goods = get_object_or_404(goods, goods_subcategory=goods_subcategory)
    context = {
        'goods_list': goods_list,
        'first_goods': first_goods,
    }
    return render(request, 'sell/subcategory_goods_list.html', context)


