from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.MainPage),
    path('app/<str:KeyApi>/', views.AppView.as_view()),
]