from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .models import HistoryWeight
from .serializers import HistoryWeightSerializer,UserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

class  CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class MyWightListView(viewsets.ModelViewSet):
    queryset = HistoryWeight.objects.all()
    serializer_class = HistoryWeightSerializer
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class MyUserIDView(APIView):
    def get(self,request,format=None):
        return Response({"id":request.user.id})
