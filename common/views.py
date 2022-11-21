from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from django.template import loader
from django.contrib import messages

from common.forms import Registrationform, Loginform


def home(request):
    template = loader.get_template('class.html')
    return HttpResponse(template.render())


def registration(request):
    if request.method == "POST":
        form = Registrationform(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
        else:
            raise ValidationError(form.errors)
    form = Registrationform()

    return render(request, 'signup.html', {'register_form': form})


def login(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect("dashboard/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm
    return render(request, 'login.html', {'login_form': form})


def dashboard(request):
    template = loader.get_template('institute_dashboard.html')
    return HttpResponse(template.render())
