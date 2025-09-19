from django.urls import path
from .views import CustomUserCreateAPIView, CustomUserDetailAPIView

urlpatterns = [
    path('user/', CustomUserCreateAPIView.as_view()),
    path('user/<int:id>/', CustomUserDetailAPIView.as_view())
]