from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('get/', views.CBView.as_view()),
    path('temv/', views.TemV.as_view()),

]
