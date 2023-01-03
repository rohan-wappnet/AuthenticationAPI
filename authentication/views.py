from django.shortcuts import render
from rest_framework import viewsets, status
from authentication.serializers import RegSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User


class RegViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegSerializer
