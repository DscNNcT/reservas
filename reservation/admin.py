from django.contrib import admin

# Register your models here.
from .models import MenuTable
admin.site.register(MenuTable)

from .models import BookingTable
admin.site.register(BookingTable)