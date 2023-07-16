from django.shortcuts import render
from .models import HistoryWeight
from .serializers import HistoryWeightSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

class MyWightListView(viewsets.ModelViewSet):
    queryset = HistoryWeight.objects.all()
    serializer_class = HistoryWeightSerializer
