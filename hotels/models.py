from django.db import models

class Rooms(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='hotels')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Reservations(models.Model):
    guest_fullname = models.CharField(max_length=255, blank=True, null=True)
    guest_email = models.EmailField( blank=True, null=True)
    arrival_date = models.DateField( blank=True, null=True)
    departure_date = models.DateField( blank=True, null=True)
    adults = models.IntegerField( blank=True, null=True)
    children = models.IntegerField( blank=True, null=True)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"Reservation for {self.guest_fullname} in room {self.rooms.name}" if self.rooms else f"Reservation for {self.guest_fullname}"

    
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    passwordConfirm = models.CharField(max_length=255)

    def __str__(self):
        return self.name
