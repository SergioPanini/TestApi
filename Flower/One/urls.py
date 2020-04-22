from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.MainPage),
    path('allapps/', views.APPModelsView.as_view()),
    path('app/<str:KeyApi>/', views.AppView.as_view()),
    path('createnewkeyapi/<str:KeyApi>/', views.CreateNewKeyApiView.as_view()),
]