from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddAppView.as_view()),
    path('test/<str:KeyApi>/', views.InfoAppView.as_view()),
    path('updatekey/<str:KeyApi>/', views.UpdateKeyApi.as_view()),

]