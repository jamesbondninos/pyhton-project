from django.urls import path

from .views import CustomerCreateAPIView, CustomerResetAPIView

urlpatterns=[
    path('customer/', CustomerCreateAPIView.as_view()),
    path('customer/reset-password/', CustomerResetAPIView.as_view())
]