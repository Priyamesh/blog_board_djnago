from multiprocessing import context
from django.shortcuts import redirect, render

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import SigunUpForm


# Create your views here.
def signup(request):
    form = SigunUpForm()

    if request.method == "POST":
        form = SigunUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    context = {"form": form}
    return render(request, "signup.html", context)


# def logoutPage(request):
#     logout(request)
#     return redirect("signup")


# def loginPage(request):
#     return render(request, "login.html", {})
