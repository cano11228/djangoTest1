from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInput

def input_page(request):
    if request.method == 'POST':
        input_text = request.POST.get('user_input')
        UserInput.objects.create(input_text=input_text)

        return redirect('display_input')
    return render(request, 'input.html')

def display_input(request):
    last_input = UserInput.objects.last()

    input_text = last_input.input_text if last_input else 'No Input Provided'
    return render(request, 'display_input.html', {'user_input': input_text})

def session_page(request):
    if 'user_input' in request.session:
        user_input = request.session['user_input']
        return HttpResponse(f"Ваше останнє введення: {user_input}")
    else:
        return HttpResponse("Ви ще не вводили дані.")