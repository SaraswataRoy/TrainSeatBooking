# seat_booking/models.py

from django.db import models

class TrainCoach(models.Model):
    COACH_SIZE = 80
    ROW_SIZE = 7
    LAST_ROW_SIZE = 3
    
    # List of tuples representing available seats in the coach
    available_seats = models.CharField(max_length=200, default="1A,1B,1C,1D,1E,1F,1G,2A,2B,2C,2D,2E,2F,2G,...,10E,10F,10G")
    
    # List of tuples representing booked seats in the coach
    booked_seats = models.CharField(max_length=200, default="")

    def __str__(self):
        return "Train Coach"
