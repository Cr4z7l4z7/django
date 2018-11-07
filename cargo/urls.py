from django.urls import path

from cargo import views

urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('base/', views.base, name='base'),
    path('car/', views.car, name='car'),
]
