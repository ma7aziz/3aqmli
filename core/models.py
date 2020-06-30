from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=220)
    email = models.CharField(max_length=220)
    phone = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    date = models.DateField()
    unit_type = models.CharField(max_length=50)
    unit_space = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
