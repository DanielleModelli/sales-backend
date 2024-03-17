from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Briefing, Retailer, Vendor, Category
from .serializers import VendorSerializer


class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer