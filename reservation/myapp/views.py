from rest_framework.response import Response
from myapp.models import Ticket
from myapp.serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class TicketView(APIView):
    def post(self,request,format=None):
        serializer=TicketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Successfully added data'},status=status.HTTP_201_CREATED)
        
    
    def get(self,request,format=None):
        tickets=Ticket.objects.all()
        serializer=TicketSerializer(tickets,many=True)
        return Response({'tickets':serializer.data,'msg':'success'},status=status.HTTP_200_OK)



