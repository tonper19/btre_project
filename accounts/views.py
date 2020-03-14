from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_again = request.POST["password2"]
        
        if password == password_again:
            # check username on the DB
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is being used")
                    return redirect("register")
                else:
                    user = User.objects.create_user(username=username
                                                    ,password=password
                                                    ,email=email
                                                    ,first_name=first_name
                                                    ,last_name=last_name)
                    # in case you need to login after register immediately:
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect("index")

                    # Brad Traversy prefers the user logs in her/himself:
                    user.save()
                    messages.success(request, "You are now registered and can log in")
                    return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")

    else:
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
