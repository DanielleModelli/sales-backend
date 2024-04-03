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
    vendors = VendorSerializer(many=True, read_only=True)
    class Meta:
        model = Retailer
        fields = ['id', 'name', 'vendors']

class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = ['id', 'name', 'retailer', 'responsible', 'category', 'release_date', 'available']

    def create(self, validated_data):
        category = validated_data.pop('category').id
        retailer = validated_data.pop('retailer').id
        instance = Briefing.objects.create(**validated_data,  category_id=category, retailer_id=retailer)
        return instance
