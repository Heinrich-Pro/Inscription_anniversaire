from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscription_view, name='inscription'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
    path('participants/', views.liste_participants_view, name='liste_participants'),
]
