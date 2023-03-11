from rest_framework import serializers
from myapp.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=['id','name','phone_number','gender','airport_name','destination_name','date','citizenship_no','citizenship_image','vaccine_cert']
        