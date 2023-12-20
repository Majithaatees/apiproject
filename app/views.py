from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import customers
from .serializers import CustomerSerializer, LoginSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method=='POST':
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'saved successfully','data':serializer.data})
@api_view(['GET'])
def display(request):
    if request.method=='GET':
        data=customers.objects.all()
        serializer=CustomerSerializer(data,many=True,context={'request':request})
        return Response(serializer.data)
@api_view(['DELETE'])
def delete(request,id):
    try:
        instance = customers.objects.get(id=id)
    except customers.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        instance.delete()
        return Response({"data":"deleted"})
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = customers.objects.filter(email=email, password=password)
        print(user)
        if user:
            # User is authenticated

            return Response({'message':"login successfull"})
        else:
            # Invalid credentials
            return Response({'error': 'Invalid credentials'})
@api_view(['PUT'])
def update(request,id):
    try:
        instance=customers.objects.get(id=id)
    except customers.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def reading(request,id):
   if request.method=='GET':
        data=customers.objects.get(id=id)
        serializer=CustomerSerializer(data,context={'request':request})
        return Response(serializer.data)
