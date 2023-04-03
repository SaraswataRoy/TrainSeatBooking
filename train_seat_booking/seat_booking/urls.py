from django.urls import path
from seat_booking import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_seats', views.book_seats, name='book_seats'),
]