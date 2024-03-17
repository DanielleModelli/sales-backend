from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDelete, CategoryListCreate, CategoryRetrieveUpdateDelte

urlpatterns = [
    path('vendors', VendorListCreate.as_view(), name="Create-Vendor-List"),
    path('vendor/<int:pk>/', VendorRetrieveUpdateDelete.as_view(), name="Vendor-Details"),

    path('categories/', CategoryListCreate.as_view(), name='Category-List'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDelte.as_view(), name='Category-Details')
]