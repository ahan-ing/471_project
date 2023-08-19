from django.contrib import admin
from homepage.models import Contact
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Division)
admin.site.register(Package)
admin.site.register(Place)
admin.site.register(PlaceCulture)
admin.site.register(PlaceFood)
admin.site.register(PlaceVideo)
admin.site.register(Hotel)
admin.site.register(HotelPhoto)
admin.site.register(Guide)
admin.site.register(Blog)
admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.register(Review)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'number', 'persons']



