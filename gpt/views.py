# from django.shortcuts import render , redirect
# from django.contrib.auth import authenticate


# def login_user(request):
#     if request.method == "POST":

#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate(username=email , password=password)

#         if user is not None:
#             return render(request , "home.html")
#         else:
#             return redirect("login_user")
#             # print("user mavjud emas")
#     else:
#         return render(request , "login.html")    


# redirect vazifasi foydalanuvchini boshqa URL ga o‘tkazish.


#  <<<<<<<<<<<<      >>>>>>>>>>>>>





from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from .models import User_profile
from main import chat_agent


def login_user(request):

    error_message = "" # Xato xabar uchun

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)

        if user is not None:
            return render(request, "home.html")
        else:
            error_message = "Email yoki parol hato"

    return render(request, "login.html", {"error_message": error_message})


# Yangi user qoshish


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")


        try:
          new_user = User_profile.objects.create_user(
              first_name = first_name,
              last_name = last_name,
              email = email,
              password = password
          )
          return redirect("login_user")
        
        except Exception as e:
            return render(request , "register.html")
        
        # Get bolsa ishlaydi
    else:
            return render(request , "register.html")



def home(request):
    if request.method == "GET":
        matematik = chat_agent(role = "matematik" , message="uchburchakka ichki chizilgan aylana radiusi")

    return render(request,"home.html" , {"matematik":matematik})












