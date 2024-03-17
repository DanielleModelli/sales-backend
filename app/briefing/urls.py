from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDelete

urlpatterns = [
    path('vendors', VendorListCreate.as_view(), name="Create-Vendor-List"),
    path('vendor/<int:pk>/', VendorRetrieveUpdateDelete.as_view(), name="Vendor-Details")
]