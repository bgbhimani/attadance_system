from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('add/', views.add_attendance,
         name='add_attendance'),

    path('search/', views.search_student,
         name='search_student'),
]