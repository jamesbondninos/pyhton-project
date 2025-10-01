from django.urls import path
from .views import VendorCreationAPIView

urlpatterns=[
    path('vendor/',VendorCreationAPIView.as_view())
]