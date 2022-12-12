from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    creada = models.DateTimeField(auto_now_add=True)
    fecha_completada = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{}- by {}".format(self.titulo,self.usuario.username) 