"""
//
//  blog_v3 -> urls
//
//  Created by 苏相荣 on 2020/3/26 18:30.
//  Copyright © 2020 SuXiangRong. All rights reserved.
//
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]