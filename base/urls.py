from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('data', views.testdata),
    path('img', views.imgView.as_view()),

]
