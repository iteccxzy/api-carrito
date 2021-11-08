from django.db.models import manager
from django.shortcuts import render

# Create your views here.

# third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import ArticleSerializer, DetalleSerializer, DetalleSerializerSave
from .models import Article, Detalle


class ArticleView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Article.objects.all()
        serializer = ArticleSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DetalleView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        # post = Detalle.objects.get(article_id=id)
        post = Detalle.objects.filter(article_id=id)
        serializer = DetalleSerializer(post, many=True)
        return Response(serializer.data)


class AddDetalleView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        print(request.data, 'testing')
        serializer = DetalleSerializerSave(data=request.data)
        if serializer.is_valid():
            try:
                
                serializer.save()
            except:
                print('no se puede guardar')
            return Response(serializer.data)
        return Response(serializer.errors)
