from django.contrib import admin
from .models import Appointment , QuickRequest
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_type' , 'recieved' )
    list_display_links = ('id','name')
    list_editable = ('recieved', )
    list_filter =('recieved',)
    list_per_page = 20


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(QuickRequest)