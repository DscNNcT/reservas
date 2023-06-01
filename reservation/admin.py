from django.contrib import admin

# Register your models here.
from .models import MenuItem
admin.site.register(MenuItem)

from .models import BookingTable
admin.site.register(BookingTable)