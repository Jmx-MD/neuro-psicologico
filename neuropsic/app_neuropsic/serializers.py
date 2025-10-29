from rest_framework import serializers
from .models import User, Adm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'nome', 'email','senha', 'data_nascimento', 'sexo']

class AdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adm
        fields = ['id_administracao', 'nome', 'email', 'senha','data_nascimento']
