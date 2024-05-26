from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Alumno(models.Model):
    nombre = models.CharField(max_length=250)
    codigo_carrera = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to='Images/')

    class Meta:
        verbose_name_plural = 'alumnos'
    
    def __str__(self):
        return self.nombre

@receiver(pre_delete, sender=Alumno)
def eliminar_imagen_alumno(sender, instance, **kwargs):
    # Eliminar la imagen asociada al alumno
    instance.imagen.delete(False)
