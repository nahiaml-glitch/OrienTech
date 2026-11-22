from django.db import models

class SolicitudContacto(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    necesidades = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"
# Create your models here.
