# seat_booking/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import TrainCoach

def index(request):
    coach = []  
    coach = TrainCoach.objects.first()
    available_seats = coach.available_seats.split(",")
    booked_seats = coach.booked_seats.split(",")
    return render(request, "seat_booking/templates/index.html", {"available_seats": available_seats, "booked_seats": booked_seats})

def book_seats(request):
    # if request.method == "POST":
    # num_seats = int(request.POST.get("num_seats"))
    num_seats = 4
    coach = TrainCoach.objects.first()
    available_seats = coach.available_seats.split(",")
    booked_seats = coach.booked_seats.split(",")
    booked = []
    for i in range(len(available_seats)):
        if available_seats[i] not in booked_seats:
            booked.append(available_seats[i])
            if len(booked) == num_seats:
                break
    if len(booked) == num_seats:
        coach.available_seats = ",".join([s for s in available_seats if s not in booked])
        coach.booked_seats += "," + ",".join(booked)
        coach.save()
        return JsonResponse({"status": "success", "booked_seats": booked, "available_seats": coach.available_seats.split(",")})
    return JsonResponse({"status": "failure", "booked_seats": [], "available_seats": coach.available_seats.split(",")})
