# recognition/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Alumno
import json
import os

@receiver(post_save, sender=Alumno)
@receiver(post_delete, sender=Alumno)
def update_alumnos_json(sender, **kwargs):
    alumnos = Alumno.objects.all()
    alumnos_list = [
        {
            "name": alumno.nombre,
            "image_path": alumno.imagen.path
        }
        for alumno in alumnos
    ]
    json_path = os.path.join(os.path.dirname(__file__), '..', 'alumnos.json')
    with open(json_path, "w") as file:
        json.dump(alumnos_list, file, indent=4)
