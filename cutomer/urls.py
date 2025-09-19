from django.urls import path

from .views import CustomerCreateAPIView, CustomerResetAPIView, CustomerLoginAPIView, CustomerForgotAPIView

urlpatterns=[
    path('customer/', CustomerCreateAPIView.as_view()),
    path('customer/reset-password/', CustomerResetAPIView.as_view()),
    path('customer/login/',CustomerLoginAPIView.as_view()),
    path('customer/forgot-password/', CustomerForgotAPIView.as_view())
]