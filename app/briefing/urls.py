from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDelete, CategoryListCreate, CategoryRetrieveUpdateDelte, RetailerListCreate, RetailerRetrieveUpdateDelete, BriefingListCreate, BriefingRetrieveUpdateDelete

urlpatterns = [
    path('vendors/', VendorListCreate.as_view(), name="Vendor-List"),
    path('vendor/<int:pk>/', VendorRetrieveUpdateDelete.as_view(), name="Vendor-Details"),

    path('categories/', CategoryListCreate.as_view(), name='Category-List'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDelte.as_view(), name='Category-Details'),

    path('retailers/', RetailerListCreate.as_view(), name='Retailer-List'),
    path('retailer/<int:pk>/', RetailerRetrieveUpdateDelete.as_view(), name='Retailer-Details'),

    path('briefings/', BriefingListCreate.as_view(), name='Briefing-List'),
    path('briefing/<int:pk>/', BriefingRetrieveUpdateDelete.as_view(), name='Briefing-Details'),
]