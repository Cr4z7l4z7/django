from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/',views.form_view, name='form_view'),
    path('signupman/', views.new_user_form, name='new_user_form'),
]
