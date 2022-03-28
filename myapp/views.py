from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import generics
from .models import Googlerecharge
from .serializers import GooglerechargeSerializer

# Create your views here.

class GooglerechargeList(generics.ListCreateAPIView):
    queryset = Googlerecharge.objects.all()
    serializer_class = GooglerechargeSerializer