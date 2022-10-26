from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home, name="front-home"),
    path('add/', views.add, name="add"),
    path("load/",views.load, name="load"),
]