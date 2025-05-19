from django.shortcuts import render, get_object_or_404, redirect
from .models import User, State, City
from django.utils.safestring import mark_safe
import json
import re
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def adduser(request):
    states = list(State.objects.values())
    cities = list(City.objects.values())

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        state = request.POST.get('state')
        city = request.POST.get('city')

        # Regex patterns
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        phone_pattern = r'^[6-9]\d{9}$'  # Indian mobile format

        # Validation
        if not re.match(email_pattern, email):
            messages.error(request, "Invalid email format.")
        elif not re.match(phone_pattern, phone):
            messages.error(request, "Invalid phone number. It should start with 6-9 and be 10 digits.")
        else:
            # If valid, save the user
            User.objects.create(
                name=name,
                email=email,
                phone=phone,
                gender=gender,
                state=state,
                city=city
            )
            messages.success(request, "User added successfully!")

    return render(request, 'adduser.html', {
        'states_json': states,
        'cities_json': cities
    })


def addstate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:  # optional: basic validation
            State.objects.create(name=name)
    return render(request, 'addstate.html')  # this line must always run

def addcity(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        state_id = request.POST.get('state_id')
        if name and state_id:
            try:
                state = State.objects.get(id=state_id)
                City.objects.create(name=name, state_id=state)
            except State.DoesNotExist:
                pass
    states = State.objects.all()
    return render(request, 'addcity.html', {'states': states})

def userinfo(request):
    users = User.objects.select_related('state', 'city').all()
    return render(request, 'userinfo.html', {'users': users})

def stateinfo(request):
    states = list(State.objects.values())
    return render(request, 'stateinfo.html', {'states_json': (states)})

def cityinfo(request):
    cities = list(City.objects.select_related('state').values('id', 'name', 'state_id_id'))
    return render(request, 'cityinfo.html', {'cities_json': (cities)})


def updateuser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    states = list(State.objects.values())
    cities = list(City.objects.values())

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.gender = request.POST.get('gender')
        user.state = request.POST.get('state')
        user.city = request.POST.get('city')
        user.save()
        return redirect('/userinfo/')  # Replace with your success redirect page

    return render(request, 'updateuser.html', {
        'user': user,
        'states_json': states,
        'cities_json': cities
    })

def deleteuser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('/userinfo/')  # Replace with your actual redirect URL name
    
