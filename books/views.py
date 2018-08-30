from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Checkout

class HomePageView(TemplateView):
    template_name = 'books/home.html'

class AboutPageView(TemplateView):
    template_name = 'books/about.html'

class CheckoutPageView(TemplateView):
    template_name = 'books/Checkout.html'

class CheckInPageView(TemplateView):
    pass