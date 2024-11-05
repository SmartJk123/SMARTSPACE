from django.contrib import admin
from django.urls import path
from smartspace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('addproperty/', views.addproperty, name='addproperty'),
]
