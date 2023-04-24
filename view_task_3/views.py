from django.shortcuts import render
from .models import *
from rest_framework.generics import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.
class AuthorListView(generics.ListAPIView):
    queryset=Author.objects.all()
    serializer_class =AuthorSerializer

    # def perform_create(self, serializer):
    #   import pdb;pdb.set_trace()
    #   queryset = Author.objects.filter(id=self.request.id)
    #   if queryset.exists():
    #       raise ValidationError('You have already signed up')
    #   serializer.save(id=self.request.id)

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=Author.objects.all()
    serializer_class =AuthorSerializer

class PublisherCreateView(generics.CreateAPIView):
    queryset=Publisher.objects.all()
    serializer_class=PublisherSerilaizer

class PublisherListView(generics.ListAPIView):
    queryset=Publisher.objects.all()
    serializer_class=PublisherSerilaizer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSeriliazer

class BookListCreateView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerilaizer

class BookRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerilaizer

class BookListView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerilaizer
    permission_classes=[IsAdminUser]
 




