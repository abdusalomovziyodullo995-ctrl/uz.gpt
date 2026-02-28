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




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import User_profile
from main import chat_agent

def login_user(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            return render(request, "home1.html")
        else:
            error_message = "Email yoki parol xato"
    return render(request, "login.html", {"error_message": error_message})

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            User_profile.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            return redirect("login_user")
        except Exception:
            return render(request, "register.html")
    return render(request, "register.html")

def home(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        role_type = request.POST.get("role")
        
        # Frontend-dan kelgan 'history' yoki 'math' ni chat_agent tushunadigan rolga aylantirish
        ai_role = "tarixchi" if role_type == "history" else "matematik"
        
        try:
            reply = chat_agent(role=ai_role, message=user_message)
            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"reply": f"Xatolik yuz berdi: {str(e)}"}, status=500)
            
    return render(request, "home1.html")



