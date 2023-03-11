
from django.urls import path
from myapp import views

urlpatterns = [
        path('api/ticketapi/',views.TicketView().as_view(),name='post'),
        path('api/ticketapi/',views.TicketView().as_view(),name='list')
]