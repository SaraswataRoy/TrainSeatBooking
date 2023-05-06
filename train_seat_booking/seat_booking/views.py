# seat_booking/views.py

from django.shortcuts import render
from django.http import JsonResponse
# from .models import TrainCoach
from rest_framework.views import APIView

def index(request):
    return render(request, "interface.html")

class Book_seats(APIView):
    try:
        def post(self, request):
            print(int(dict(request.data)['seats'][0]))
            if len(dict(request.data)['seats']) != 0 and int(dict(request.data)['seats'][0]) > 0:
                num_seats = int(dict(request.data)['seats'][0])
                # coach = TrainCoach.objects.first()
                available_seats = request.data['available_seats'].split(",")
                booked_seats = request.data['booked_seats'].split(",")
                booked = []
                # for key,val in checkavailibility(available_seats)
                for i in range(len(available_seats)):
                    if available_seats[i] not in booked_seats:
                        booked.append(available_seats[i])
                        if len(booked) == num_seats:
                            break
                if len(booked) == num_seats:
                    available_seats = ", ".join([s for s in available_seats if s not in booked])
                    # booked_seats = booked_seats + booked
                    booked = ", ".join([s for s in booked])
                    # coach.save()
                    print(checkavailibility(request.data, num_seats))
                    return JsonResponse({"status": "success", "booked_seats": booked, "available_seats": available_seats})
            else:
                return JsonResponse({"status": "failure"})
    except Exception as e:
        raise Exception(f'Error in REST/Book_seats {e}')

def checkavailibility(coach, num_seats):
    available_seats = coach['available_seats'].split(",")
    # print(available_seats)
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
        updtd_availableseats = []
        if seatcount >= num_seats:
            for seats in available_seats:
                if(str(rowid) in seats and counter < num_seats):
                    booked_seats.append(seats)
                    # available_seats.remove(seats)
                    counter += 1
                else:
                    updtd_availableseats.append(seats)
            # print(updtd_availableseats)
            return booked_seats
    