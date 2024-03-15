from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name


class LogSolicitud(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=255)
    solicitud = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.host} - {self.solicitud} - {self.fecha}"