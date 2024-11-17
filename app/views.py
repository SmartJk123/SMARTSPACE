from django.shortcuts import render

def homepage(request):
    """Render the homepage."""
    return render(request, 'app/homepage.html')

def bookingpage(request):
    """Render the booking page."""
    return render(request, 'app/bookingpage.html')

def dashboard(request):
    """Render the user dashboard."""
    return render(request, 'app/dashboard.html')

def admindashboard(request):
    """Render the admin dashboard."""
    return render(request, 'app/admindashboard.html')

def adminbookings(request):
    """Render the admin bookings page."""
    return render(request, 'app/adminbookings.html')

def customers(request):
    """Render the customers list page."""
    return render(request, 'app/customers.html')

def customerdetail(request):
    """Render the customer detail page."""
    return render(request, 'app/customerdetail.html')

def payment(request):
    """Render the payment page."""
    return render(request, 'app/payment.html')

def addproperty(request):
    """Render the add property page."""
    return render(request, 'app/addproperty.html')

def housedetail(request):
    """Render the house detail page."""
    return render(request, 'app/housedetail.html')
