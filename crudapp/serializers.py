from rest_framework import serializers
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'age', 'phone')
        model = Person