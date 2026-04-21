
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('blog/', views.blog, name='blog'),
    path('detail/', views.detail, name='detail'),
    path('price/', views.price, name='price'),
    path('search/', views.search, name='search'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('starter/', views.starter, name='starter'),
]
