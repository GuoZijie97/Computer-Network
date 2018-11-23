#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:17:17 2018

@author: limengxin
"""

from django.urls import path

from . import views

app_name = 'sell'
urlpatterns = [
    # ex: /sell/
    path('', views.index, name='index'),
    # ex: /sell/upload/
    path('upload/', views.upload, name='upload'),
    #path('good/', views.good, name='good'),
    # ex: /sell/1/subcategory/
    path('<str:goods_subcategory>/subcategory/', views.subcategory_view, name='subcategory_view'),
]