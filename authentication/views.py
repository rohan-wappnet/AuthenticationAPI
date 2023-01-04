from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import RegSerializer, GetLoginTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class RegViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegSerializer

class LoginTokenViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetLoginTokenSerializer
    queryset = get_user_model().objects.all()