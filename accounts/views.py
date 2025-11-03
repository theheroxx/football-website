
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# صفحه ورود
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my_profile')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
    return render(request, 'accounts/login.html')


# صفحه ثبت‌نام
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request, 'رمز عبور با تکرار آن یکسان نیست')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً استفاده شده است')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('my_profile')
    return render(request, 'accounts/register.html')


# خروج کاربر
def logout_view(request):
    logout(request)
    return redirect('login')


# صفحه پروفایل من
def my_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/my_profile.html', {'user': request.user})
