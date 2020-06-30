from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment
# Create your views here.


def index(request):
    return render(request, 'index.html')


def book(request):
    print(request.POST)
    pass


def appointment(request):
    if request.is_ajax():
        print(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        date = request.POST.get('date')
        unit_type = request.POST.get('type')
        unit_space = request.POST.get('space')
        appointment = Appointment(name=name, phone=phone, email=email , address = address , 
                                    date = date, unit_space=unit_space, unit_type=unit_type )
        appointment.save()  

        response = {
            
            'msg': 'your Request Has been Sent .. We will Contact you as soon as possible.'
        }
        return JsonResponse(response)
        
    return render(request, 'appointment.html')

def about_us(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')
