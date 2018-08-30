from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('checkout/', views.CheckoutPageView.as_view(), name='checkout')
    path('checkin/', views.CheckInPageView.as_view(), name='checkin')
]