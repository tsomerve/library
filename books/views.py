from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Checkout

class HomePageView(TemplateView):
    template_name = 'books/home.html'

class AboutPageView(TemplateView):
    template_name = 'books/about.html'

