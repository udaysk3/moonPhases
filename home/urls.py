
from home import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('home',views.index, name='index'),
    path('home2',views.index2, name='index2'),
    path('feedback', views.feedback,name='feedback'),
    path('upcoming',views.upcoming, name='upcoming'),
    path('',views.enter, name="enter" )
]
