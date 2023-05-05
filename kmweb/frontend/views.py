from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, SigninForm, RideForm
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def home(request):
     is_authenticated = request.user.is_authenticated
     if request.user.is_authenticated:
         return render(request, 'home.html', {'is_authenticated': is_authenticated, })
     else:
         return render(request, 'home.html', {'signin_form': SigninForm(), 'signup_form': SignupForm(), 'ride_form':RideForm()})

def signin(request):
     if request.method == 'POST':
         form = SigninForm(request.POST)
         if form.is_valid():
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             user = authenticate(request, username=username, password=password)
             if user is not None:
                 login(request, user)
                 return redirect('home')
             else:
                 messages.error(request, 'Invalid username or password')
     return redirect('home')

def signup(request):
     if request.method == 'POST':
         form = SignupForm(request.POST)
         if form.is_valid():
             username = form.cleaned_data['username']
             phone_number = form.cleaned_data['phone_number']
             password = form.cleaned_data['password']
             user = User.objects.create_user(username=username, password=password)
             user.phone_number = phone_number
             user.save()
             messages.success(request, 'Your account has been created successfully. Please login to continue.')
             return redirect('home')
     return redirect('home')

def signout(request):
     logout(request)
     return redirect('home')



@login_required
def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.host = request.user # set the host field to the currently logged-in user
            ride.save()
            return redirect('ride_detail', ride_id=ride.id)
    else:
        form = RideForm()
    return render(request, 'home.html', {'ride_form': RideForm()})


@login_required
def join_ride(request):
    if request.method == 'POST':
        ride_link = request.POST.get('ride-link')
        ride_id = int(ride_link.split('/')[-2])
        ride = Ride.objects.get(id=ride_id)
        ride.participants.add(request.user)
        ride.save()
        return redirect(reverse('ride_detail', args=[ride_id]))
    else:
        return redirect('home')


def ride_detail(request,  ride_id):
    ride = get_object_or_404(Ride, pk=ride_id)  
    context= {
    'ride':ride,
    }
    return render(request, 'ride.html', context)


