from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.homepage, name='homepage'),  # URL for homepage
    path('bookingpage', views.bookingpage, name='bookingpage'),  # URL for booking page
    path('dashboard', views.dashboard, name='dashboard'),  # URL for user dashboard
    path('admindashboard', views.admindashboard, name='admindashboard'),  # URL for admin dashboard
    path('adminbookings', views.adminbookings, name='adminbookings'),  # URL for admin bookings
    path('customers', views.customers, name='customers'),  # URL for customer list
    path('customerdetail', views.customerdetail, name='customerdetail'),  # URL for customer detail
    path('payment', views.payment, name='payment'),  # URL for payment
    path('addproperty', views.addproperty, name='addproperty'),  # URL for add property
    path('housedetail', views.housedetail, name='housedetail'),  # URL for house detail
]
