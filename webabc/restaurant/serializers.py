from rest_framework import serializers
from .models import city, menu

class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = '__all__'

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'