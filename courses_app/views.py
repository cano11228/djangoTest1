from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# В'юшка для перевірки аутентифікації користувача
def courses_page(request):
    # Перевірка, чи користувач аутентифікований
    if request.user.is_authenticated:
        return HttpResponse("This is the Courses page")
    else:
        # Якщо користувач не аутентифікований, перенаправлення на сторінку входу
        return HttpResponse("You have no permissions to view this page")