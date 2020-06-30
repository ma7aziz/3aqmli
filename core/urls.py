from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name='index'),
    path('about-us', views.about_us, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('appointment', views.appointment, name='appointment'),
    path('quick-contact', views.quick_contact, name='quick-contact')
]
