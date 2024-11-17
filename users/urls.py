from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
    path('password-reset/', 
        PasswordResetView.as_view(
            template_name='users/account/password_reset.html',
            html_email_template_name='users/account/password_reset_email.html'
        ),
        name='password-reset'
    ),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/account/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/account/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/account/password_reset_complete.html'),name='password_reset_complete'),

    # path("register", views.register, name="register"),
    # path('login', views.custom_login, name='login'),
    # path('logout', views.custom_logout, name='logout'),
    # path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)