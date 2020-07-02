from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment ,QuickRequest
from django.core.mail import EmailMultiAlternatives, mail_admins, send_mail , EmailMessage
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request, 'index.html')


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
    if request.is_ajax():
        print(request.POST)
        response = {
            'msg': 'your message has been sent successfully .. We will reach out to you soon .'
        }
        return JsonResponse(response)

    return render(request, 'contact.html')

def quick_contact(request):
    if request.is_ajax():
        phone = request.POST.get('phone')
        email_msg = EmailMessage(
        subject='New Contact Phone Number Recieved',
        body=f'We recieved new quick contact phone number ,{phone}', 
        from_email='info@3aqmli.com',  
        to=['ma7moud.aelaziz@gmail.com'],)
        
        email_msg.send()
        contact = QuickRequest(phone = phone)
        contact.save()
        response = {
            'msg': 'your phone number has been sent successfully .. We will reach out to you soon .'
        }
        return JsonResponse(response)

@user_passes_test(lambda u: u.is_superuser)
def appointments(request):
    appointments = Appointment.objects.all().order_by('-timestamp')
    paginator = Paginator(appointments, 15 )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'appointments.html' , 
        {'page_obj': page_obj, 
        
        }
    ) 

@user_passes_test(lambda u: u.is_superuser)
def appoint_details(request, id):
    appointment = Appointment.objects.get(pk=id)
    return render(request, 'apt_details.html' , {'appointment': appointment})



@user_passes_test(lambda u: u.is_superuser)
def quick_request(request):
    numbers = QuickRequest.objects.all().order_by('-timestamp')
    paginator = Paginator(numbers, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quick_request.html' , 
        {'page_obj': page_obj, 
        
        }
    ) 