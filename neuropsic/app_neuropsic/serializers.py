from rest_framework import serializers
from .models import User, Adm
import ast
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_internal_value(self, data):
        cleaned = {}

        for key, value in data.items():
            # Se for lista, transforma em string separada por vírgula
            if isinstance(value, list):
                value = ','.join(value)
            # Remove espaços extras
            if isinstance(value, str):
                value = value.strip()
            cleaned[key] = value

        return super().to_internal_value(cleaned)

class AdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adm
        fields = '__all__'
