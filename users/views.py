from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm,UserUpdateForm
from .decorators import user_not_authenticated

from .models import*



app_name='users'




# @user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(request=request,template_name="users/register.html",context={"form": form})

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

# @user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                # messages.success(request, f"Hello {user.username} You have been logged in")
                return redirect("gallery")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = UserLoginForm()

    return render(request=request,template_name="users/login.html",context={"form": form})



def profile(request, pk):
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'Your profile has been updated!')
            # Check if the user is redirected correctly
            print(f"Redirecting to profile for user {user_form.pk}")
            return redirect("profile", user_form.pk)
        else:
            # Print form errors for debugging
            for error in list(form.errors.values()):
                print(error)
            messages.error(request, "There was an error updating your profile.")

    user = get_user_model().objects.filter(pk=pk).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(
            request=request,
            template_name="profile.html",
            context={"form": form}
        )
    
    return redirect("/")



