from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>', views.book_detail, name='book_detail'),
    path('check_out/<int:pk>', views.check_out, name='check_out'),
    path('check_in/<int:pk>', views.check_in, name='check_in'),
]