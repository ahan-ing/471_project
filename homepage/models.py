from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    phone_number = PhoneNumberField(region='BD')


class Contact(models.Model):
    name = models.CharField(max_length=115)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    

    def __str__(self):
        return self.name


class Division(models.Model):
    class DivisionName(models.TextChoices):
        DHAKA = "DHAKA", "Dhaka Division"
        BARISAL = "BARISAL", "Barisal Division"
        KHULNA = "KHULNA", "Khulna Divison"
        MYMENSINGH = "MYMENSINGH", "Mymensingh Division"
        RAJSHAHI = "RAJSHAHI", "Rajshahi Division"
        RANGPUR = "RANGPUR", "Rangpur Divison"
        SYLHET = "SYLHET", "Sylhet Division"
        CHITTAGONG = "CHITTAGONG", "Chittagong"
    name = models.CharField(
        max_length=30, choices=DivisionName.choices, unique=True)

    def __str__(self):
        return self.name.capitalize()


class Place(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(null=True, upload_to="placeimage/")
    add_to_nav = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PlaceCulture(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to="placeimage/")
    description = models.TextField(null=True)


    def __str__(self):
        return self.place.name


class PlaceFood(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    photo = models.ImageField(null=True, upload_to="placeimage/")

    def __str__(self):
        return self.name


class PlaceVideo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    video = models.URLField(null=True)

    def __str__(self):
        return self.title


class Hotel(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name


class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to='hotelimage/')

    def __str__(self):
        return self.hotel.name


class Guide(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=10, null=True)
    photo = models.ImageField(null=True, upload_to='guides/')
    phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name

# end Model for each place

# model for package


class Package(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(null=True, upload_to='packeage/')
    name = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    destination = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0)
    plan = models.TextField(null=True)
    terms = models.TextField(null=True)
    seats = models.IntegerField(null=True, default=10)
    remaining_seats = models.IntegerField(null=True)

    def __str__(self):
        return self.name


# end model for package


class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.package.name}"


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    package = models.CharField(max_length=50, null=True, blank=True)
    persons = models.IntegerField(default=1)
    number = models.CharField(max_length=15, null=True)
    booked_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)


CITIES = [
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    ('Nārāyanganj', 'Nārāyanganj'),
    ('Khulna', 'Khulna'),
    ('Gāzipura', 'Gāzipura'),
    ('Rangapukur', 'Rangapukur'),
    ('Mymensingh', 'Mymensingh'),
    ('Bogra', 'Bogra'),
    ('Tungi', 'Tungi'),
    ('Siddhirganj', 'Siddhirganj'),
    ('Narsingdi', 'Narsingdi'),
    ('Sirajganj', 'Sirajganj'),
]

BUSES = [
    ("Hanif", "Hanif"),
    ("Ena", "Ena"),
    ("Bashumati", "Bashumati"),
]

class Ticket(models.Model):
    bus_name = models.CharField(max_length=30, null=True, choices=BUSES)
    source = models.CharField(max_length=20, null= True, choices=CITIES)
    destination = models.CharField(max_length=20, null= True, choices=CITIES)
    going_date = models.DateField(null=True)
    return_date = models.DateField(null=True, blank= True)



class Blog(models.Model):
    author_name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    video = models.FileField(null=True, blank=True, upload_to='blog/')
    is_approved = models.BooleanField(default=False)
    upload_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title