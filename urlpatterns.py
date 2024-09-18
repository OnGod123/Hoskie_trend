# urls.py
from django.urls import path
from .views import submit_message, get_trends

urlpatterns = [
    path('submit/', submit_message, name='submit_message'),
    path('trends/', get_trends, name='get_trends'),
]
