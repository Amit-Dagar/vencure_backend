from django.urls import path
from .api import (
    CreateVendor,
    UpdateVendorPassword,
    ReadVendors,
    VendorStatus
)


urlpatterns = [
    path('createVendor', CreateVendor.as_view()),
    path('read', ReadVendors.as_view()),
    path('update_vendor/<str:id>', VendorStatus.as_view()),
    path('update_password/<str:id>', UpdateVendorPassword.as_view()),
]
