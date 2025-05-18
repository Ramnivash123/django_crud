from django.shortcuts import render, redirect
from .models import User, State, City
from django.utils.safestring import mark_safe
import json

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
        User.objects.create(
                name=name,
                email=email,
                phone=phone,
                gender=gender,
                state=state,
                city=city
            )

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
    users = list(User.objects.values())
    return render(request, 'userinfo.html', {'users_json': users})  # Remove json.dumps

def stateinfo(request):
    states = list(State.objects.values())
    return render(request, 'stateinfo.html', {'states_json': (states)})

def cityinfo(request):
    cities = list(City.objects.select_related('state').values('id', 'name', 'state_id_id'))
    return render(request, 'cityinfo.html', {'cities_json': (cities)})
