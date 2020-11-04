from django.urls import path
from . import views

urlpatterns = [
    path('create-studnet', views.create_studnet, name='create')
]