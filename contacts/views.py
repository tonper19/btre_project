from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id
                                                        ,user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing")
                return redirect(f"/listings/{listing_id}")

        contact = Contact(listing=listing, listing_id=listing_id, name=name
                        ,email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
        send_mail(
            subject=f"Property Listing Inquiry: {listing}",
            message=(f"There has been an inquiry for {listing}.\n" \
                     f"Name: {name}\n"
                     f"Email address: {email}\n"
                     f"Telephone number: {phone}\n"
                     f"Message: {message}\n\n"
                     f"Sign into the Admin Panel for more info."),
            from_email="technology.artisans.django@gmail.com",
            recipient_list=[realtor_email, "tonper19@gmail.com"],
            fail_silently=False,
        )

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon")
        return redirect(f"/listings/{listing_id}")
