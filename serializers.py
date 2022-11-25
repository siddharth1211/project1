from .models import apiData
from rest_framework import serializers

class apiSerializer(serializers.ModelSerializer):

    class Meta:
        model = apiData
        fields = '__all__'