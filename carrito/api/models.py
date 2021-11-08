from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    precio = models.FloatField()
    creado = models.DateTimeField( auto_now=True )
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.modelo}, {self.marca} '

class Detalle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    talle = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.color}, {self.talle} '
