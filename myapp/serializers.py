from pyexpat import model
from rest_framework import serializers
from .models import Googlerecharge



class GooglerechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Googlerecharge
        fields = '__all__'