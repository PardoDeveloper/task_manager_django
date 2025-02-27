from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Se crea automáticamente
    updated_at = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"
