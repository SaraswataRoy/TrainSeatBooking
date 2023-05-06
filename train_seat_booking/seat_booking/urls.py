from django.urls import path
from seat_booking import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('interface', views.index, name='index'),
    path('interface/book_seats', views.Book_seats.as_view(), name='book_seats'),
]