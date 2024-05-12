from django.shortcuts import render, redirect
from django.http import HttpResponse

# Сторінка вводу
def input_page(request):
    # Перевірка на POST запит
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        # Збереження даних у сесії
        request.session['user_input'] = user_input

        # Перенаправлення на сторінку відображення вводу
        return redirect('display_input')
    # Якщо GET запит, відображаємо порожню форму
    return render(request, 'input.html')

# Сторінка відображення користувацького вводу
def display_input(request):
    # Отримання введення з сесії
    user_input = request.session.get('user_input', 'No Input Provided')
    # Відправлення даних до шаблону
    return render(request, 'display_input.html', {'user_input': user_input})
# Сторінка для роботи з request.session
def session_page(request):
    if 'user_input' in request.session:
        user_input = request.session['user_input']
        return HttpResponse(f"Ваше останнє введення: {user_input}")
    else:
        return HttpResponse("Ви ще не вводили дані.")