from rest_framework import serializers

from .models import Article, Detalle

class ArticleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Article
        fields = ('marca', 'modelo', 'precio')

class DetalleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Detalle
        fields = ('color', 'talle', 'cantidad')