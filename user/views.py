from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout


def custom_register(request):
    if request.method == 'POST':
        req_data = request.POST
        email = req_data.get('email')

        user = User.objects.filter(email=email).first()
        if user:
            messages.error(request, "Bunday foydalanuvchi mavjud.")
            return redirect('register')
        # if password1 != password2:
        #     messages.info(request, "Parollar bir xil emas!")
        #     return redirect("register")
        
        # 1)
        # new_user = User(
        #     first_name=first_name,
        #     email=email,
        # )
        # new_user.set_password(password1)
        # new_user.save()
        
        # 2)
        # User.objects.create_user(first_name, email, password1)
        form = UserRegisterForm(req_data)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    return render(request, 'register.html')


def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        # user = authenticate(request, email=email, password=password)
        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, 'Bunday foydalanuvchi mavjud emas!')
            return redirect('login')
        elif not user.check_password(password):
            messages.info(request, "Parol xato!")
            return redirect("login")
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("home")
    return render(request, 'login.html')


def custom_logout(request):
    logout(request)
    return redirect("login")