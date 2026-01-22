from django.urls import path
from . import views

urlpatterns = [
    path('', views.askQuestion, name='ask'),
    path('questions/', views.questions_list, name='list'),
    path('questions/delete/<slug:slug>/', views.deleteQuestion, name='delete'),
]