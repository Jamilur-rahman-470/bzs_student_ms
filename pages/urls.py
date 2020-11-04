from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('403', views.unauth, name='unauth')
]