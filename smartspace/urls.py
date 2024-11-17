# project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views  # Import the views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('app.urls')),  # Main app routes
    path('',include('users.urls')),

]


# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
