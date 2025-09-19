from django.urls import path
from .views import PersonListCreateAPIView, PersonDetailsAPIView

urlpatterns = [
    path('person/', PersonListCreateAPIView.as_view()),
    path('get_all/', PersonListCreateAPIView.as_view()),
    path('get/<int:id>/', PersonDetailsAPIView.as_view())
]