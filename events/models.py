from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    imgprofile = models.ImageField(
        upload_to='imgprofole', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Events(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo


class Reserve(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Events, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.evento.titulo}'
