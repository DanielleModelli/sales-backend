from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Briefing, Retailer, Vendor, Category
from .serializers import VendorSerializer, CategorySerializer, RetailerSerializer, BriefingSerializer

class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDelte(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RetailerListCreate(generics.ListCreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

class RetailerRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

class BriefingListCreate(generics.ListCreateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer

class BriefingRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer