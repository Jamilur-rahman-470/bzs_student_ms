from django.urls import path
from . import views

urlpatterns = [
    path('class/management', views.class_management, name='classes'),
    path('class/delete-all', views.delete_all_class, name='c.d.all'),
    path('class/delete/<int:id>', views.delete_class, name='c.d'),
    path('class/search/', views.search_class, name='c.s'),
    path('class/import/', views.import_classes, name='c.i'),
    path('class/add/', views.add_class, name='c.a'),

    path('student/management', views.studen_management, name='students'),
    path('class/delete-all', views.delete_all_student, name='s.d.all'),
]