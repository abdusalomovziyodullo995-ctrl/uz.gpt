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



#  <<<<<<<<<<<<      >>>>>>>>>>>>>





from django.shortcuts import render
from django.contrib.auth import authenticate

def login_user(request):
    error_message = ""  # Xato xabar uchun

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)

        if user is not None:
            return render(request, "home.html")
        else:
            error_message = "Email yoki parol hato"

    return render(request, "login.html", {"error_message": error_message})









