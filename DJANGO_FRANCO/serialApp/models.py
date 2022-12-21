from django.db import models

# Create your models here.


class  Participante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=50)
    hora_inscripcion = models.TimeField()
    email = models.EmailField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=300)
