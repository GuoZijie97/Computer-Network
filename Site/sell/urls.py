#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:17:17 2018

@author: limengxin
"""

from django.urls import path
from django.conf.urls import url
from django.views.static import serve

from . import views
from shesite.settings import BASE_DIR
import os

app_name = 'sell'
urlpatterns = [
    # ex: /sell/
    path('', views.index, name='index'),
    path('graduation/', views.graduation, name='graduation'),
    # ex: /sell/upload/
    path('upload/', views.upload, name='upload'),
    # ex: /sell/confirm/
    path('confirm/', views.confirm, name='confirm'),
    # ex: /sell/1/subcategory/
    path('<str:goods_subcategory>/subcategory/', views.subcategory_view, name='subcategory_view'),
    # ex: /sell/5/single-product-details/
    path('<int:pk>/single-product-details/', views.detail, name='detail'),
    url(r'^[0-9]*/single-product-details/(?P<path>.*)$', serve, {"document_root": BASE_DIR}),
    # ex: /sell/is_selling/
    path('is_selling/', views.is_selling, name='is_selling'),
]