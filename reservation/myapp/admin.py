from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_number','gender','airport_name','destination_name','date','citizenship_no','citizenship_image','vaccine_cert']
