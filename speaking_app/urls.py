from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name="home"),
    path('', views.HomeView.as_view(), name="home"),
    path('contact', views.MessagesCreateView.as_view(), name="contact form"),
    path('test', views.TestView, name="test"),
]
