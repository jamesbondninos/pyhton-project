from django.urls import path
from .views import StudentsListAPIView, StudentsLoginAPIView

urlpatterns = [
    path('student/',StudentsListAPIView.as_view()),
    path('student/login', StudentsLoginAPIView.as_view())  
]