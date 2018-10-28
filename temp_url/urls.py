from django.urls import path

from temp_url import views

app_name='temp_url'

urlpatterns= [
path('base/',views.base, name='base'),
path('index2/',views.index2, name='index2'),
path('other/', views.other, name='other'),
path('relative/', views.relative, name='relative'),
path('register/', views.register, name='register'),
path('logout/', views.user_logout, name='user_logout'),
path('special/', views.special, name='special'),
path('login/', views.user_login,name='user_login'),
]
