from django.urls import path
from . import views

urlpatterns = [
    # Если путь пустой (''), вызываем функцию views.index
    path('', views.index, name='home'),
]