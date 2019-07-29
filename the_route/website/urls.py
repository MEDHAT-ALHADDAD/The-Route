from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path('Home/', views.Home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('rec/', views.rec, name = 'rec'),
    path('results/', views.results, name = 'results'),
]
