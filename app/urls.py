from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addproperty/', views.addproperty, name='addproperty'),
]
