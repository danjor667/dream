from django.shortcuts import render
from django_tenants.utils import schema_context
from rest_framework import generics, renderers, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import  SchoolSerializer
from dreametrix.models import School


class SchoolList(APIView):

    def get(self):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)


