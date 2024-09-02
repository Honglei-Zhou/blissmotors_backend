from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions
from .models import Car
from .serializers import CarSerializer
from oauth2_provider.contrib.rest_framework import OAuth2Authentication


# Create your views here.
class DefaultsMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class OAuth2Mixin(object):

    permission_classes = (
        OAuth2Authentication,
    )


class CarViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Car.objects.order_by('year')
    serializer_class = CarSerializer



