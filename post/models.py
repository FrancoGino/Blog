from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post (models.Model):
    titulo = models.CharField(max_length=60)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo