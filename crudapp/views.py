from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, \
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PersonSerializer
from .models import Person


class PersonAddAPIView(CreateAPIView):
    permission_classes = ()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class GetPersonView(RetrieveAPIView):
    permission_classes = ()
    serializer_class = PersonSerializer

    def get_object(self):
        queryset = Person.objects.get(pk=self.kwargs.get('pk'))
        return queryset