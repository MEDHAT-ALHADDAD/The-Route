from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('home/', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('rec/', views.rec, name = 'rec'),
    path('results/', views.results, name = 'results'),
    path('contactus/', views.contactus, name = 'contactus'),
    path('afterReg/', views.afterReg, name = 'afterReg'),
]
