from django.shortcuts import render
# the viewsets base class provides the implementatio for CRUD opearations by default. This code specifies the serializer_class and queryset
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
