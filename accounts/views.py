from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        # Register user logic goes here
        print("*** (POST) registration submit coming soon!")
        messages.error(request, "Error Message Test")
        return redirect("register")

    print("*** (GET) render registration.html")
    return render(request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        # Login user logic goes here
        print("*** login submit coming soon!")
        return redirect("login")

    return render(request, "accounts/login.html")

def logout(request):
    return redirect("index")

def dashboard(request):
    return render(request, "accounts/dashboard.html")

