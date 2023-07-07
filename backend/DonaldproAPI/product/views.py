from .models import Product
from django.http import JsonResponse

from django.forms.models import model_to_dict

from rest_framework.response import Response  
from rest_framework.decorators import api_view
from .serializer import ProductSerializer

from rest_framework import  generics

class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()   
    serializer_class = ProductSerializer

class CreateProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)

class UpdateProductView(generics.UpdateAPIView):  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'
    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = name
        serializer.save(content=content)  

class DeleteProductView(generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     return super().get_queryset().filter(name__icontains='man')
