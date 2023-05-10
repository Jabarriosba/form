from django.db import models


class Registro(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateTimeField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField()
    direccion = models.CharField(max_length=30)
    casa_apto = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}{self.apellido}"
