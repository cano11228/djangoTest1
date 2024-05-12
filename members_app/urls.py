# members_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_page, name='input_page'),
    path('display/', views.display_input, name='display_input'),
    path('session/', views.session_page, name='session_page'),
]
