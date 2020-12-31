from .models import *
from .serializers import *
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class DrugsView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = Drugs.objects.all()
	serializer_class = DrugsSerializer

@method_decorator(login_required, name='dispatch')
class PuskesmasView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = Puskesmas.objects.all()
	serializer_class = PkmSerializer

@method_decorator(login_required, name='dispatch')
class DrugsQuantityView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = DrugsQuantity.objects.all()
	serializer_class = DQSerializer