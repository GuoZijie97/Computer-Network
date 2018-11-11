#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:17:17 2018

@author: limengxin
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]