from django.urls import path
from .views import create_appointment

urlpatterns = [
    path("appointmentcreate/", create_appointment, name="appointmentCreate"),
]
