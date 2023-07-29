from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .plots import *


def index(request):
    nw_lat = request.GET.get("nw_lat")
    nw_long = request.GET.get("nw_long")
    se_lat = request.GET.get("se_lat")
    se_long = request.GET.get("se_long")
    if not nw_lat or not nw_long or not se_lat or not se_long:
        nw_lat = "41.975121"
        nw_long = "-87.791649"
        se_lat = "41.978260"
        se_long = "-87.763931"
    return render(request=request, template_name="chart/index.html", context={"nw_lat": nw_lat, "nw_long": nw_long,
                                                                              "se_lat": se_lat, "se_long": se_long})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("chart:index")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render(request=request, template_name="chart/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="chart/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


def draw_request(request):
    response = HttpResponse(content_type="image/png")
    draw_type = request.GET.get("type")
    nw_lat = request.GET.get("nw_lat")
    nw_long = request.GET.get("nw_long")
    se_lat = request.GET.get("se_lat")
    se_long = request.GET.get("se_long")
    if draw_type == "pie":
        pie(response, nw_lat, nw_long, se_lat, se_long)
    elif draw_type == "scatter":
        scatter(response, nw_lat, nw_long, se_lat, se_long)
    elif draw_type == "barh":
        barh(response, nw_lat, nw_long, se_lat, se_long)
    elif draw_type == "grid":
        grid(response, nw_lat, nw_long, se_lat, se_long)
    return response
