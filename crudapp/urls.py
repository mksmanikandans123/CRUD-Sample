from django.urls import path
from django.conf.urls import url, include

from .views import PersonAddAPIView, GetPersonView

urlpatterns = [
    path('person/add/', PersonAddAPIView.as_view()),
    path('person/person-view/<int:pk>/', GetPersonView.as_view()),
]
