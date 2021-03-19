from django.urls import path
from .api import (
    CreateVendor
)


urlpatterns = [
    path('createVendor', CreateVendor.as_view()),
]
