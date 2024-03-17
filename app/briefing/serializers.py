from rest_framework import serializers
from .models import Vendor, Category, Retailer, Briefing

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['id', 'name', 'vendors']

class BriefingSerializer(serializers.ModelSerializer):
    retailer = RetailerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Briefing
        fields = ['id', 'name', 'retailer', 'responsible', 'category', 'release_date', 'available']