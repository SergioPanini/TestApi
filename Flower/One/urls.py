from django.urls import path
from . import views

urlpatterns = [
    path('app/<str:KeyApi>/', views.AppView.as_view()),
    path('updatekey/<str:KeyApi>/', views.UpdateKeyApi.as_view()),
]