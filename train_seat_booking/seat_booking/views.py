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
    num_seats = 3
    coach = TrainCoach.objects.first()
    available_seats = coach.available_seats.split(",")
    booked_seats = coach.booked_seats.split(",")
    booked = []
    # for key,val in checkavailibility(available_seats)
    for i in range(len(available_seats)):
        if available_seats[i] not in booked_seats:
            booked.append(available_seats[i])
            if len(booked) == num_seats:
                break
    if len(booked) == num_seats:
        coach.available_seats = ",".join([s for s in available_seats if s not in booked])
        coach.booked_seats += "," + ",".join(booked)
        # coach.save()
        print(checkavailibility(coach.available_seats, num_seats))
        return JsonResponse({"status": "success", "booked_seats": booked, "available_seats": coach.available_seats.split(",")})
    return JsonResponse({"status": "failure", "booked_seats": [], "available_seats": coach.available_seats.split(",")})

def checkavailibility(available_seats, num_seats):
    available_seats = available_seats.split(',') if type(available_seats) == str else available_seats
    zeroth_row = int(available_seats[0].split('-')[0])
    available_count = 0
    available_rec = {}
    for seat in available_seats:
        row = int(seat.split('-')[0])
        if row == zeroth_row:
            available_count += 1
            available_rec[row] = available_count
        else:
            available_count = 0
            available_count += 1
            zeroth_row = row
    for rowid,seatcount in available_rec.items():
        counter = 0
        booked_seats = []
        if seatcount >= num_seats:
            for seats in available_seats:
                if(str(rowid) in seats and counter < num_seats):
                    print(rowid)
                    booked_seats.append(seats)
                    counter += 1
            return booked_seats
        else:
            return False
    