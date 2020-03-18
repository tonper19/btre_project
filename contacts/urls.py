from django.urls import path
from . import views

urlpatterns = [
    # contact is linked to the method views.contact
    path("contact", views.contact, name="contact")
]
