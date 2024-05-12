# members_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_page, name='courses_page'),
]
