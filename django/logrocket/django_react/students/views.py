from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import Student
from .serializers import *

@api_view(['GET', 'POST'])
def students_list(req):
    if req.method == 'GET':
        data = Student.objects.all()
        
        serializer = StudentSerializer(data, context = {'req': req},many = True)
        return Response(serializer.data)
    
    elif req.method == 'POST':
        serializer = StudentSerializer(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE'])
def students_detail(req, pk):
    try: 
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if req.method == 'PUT':
        serializer = StudentSerializer(student, data = req.data, context = {'req': req})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif req.method == 'DELETE':
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)