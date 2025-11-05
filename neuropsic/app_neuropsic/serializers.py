from rest_framework import serializers
from .models import User, Adm
import ast
import json

class MultiSelectFieldSerializer(serializers.Field):
    # def to_representation(self, value):
    #     # transforma string "A,B,C" em lista ['A','B','C']
    #     if isinstance(value, str):
    #         return value.split(',')
    #     return value

    # def to_internal_value(self, data):
    #     # transforma lista ['A','B'] em string "A,B"
    #     if isinstance(data, list):
    #         return ','.join(data)
    #     return data

    SEPARATOR = ';'

    def to_representation(self, value):
        if not value:
            return []

        if isinstance(value, (list, tuple)) and len(value) == 1 and isinstance(value[0], str):
            value = value[0]

        if isinstance(value, str):
            if self.SEPARATOR in value:
                return [v.strip() for v in value.split(self.SEPARATOR) if v.strip()]
            else:
                return [value.strip()]

        if isinstance(value, (list, tuple)):
            return [v.strip() for v in value]

        return []

    def to_internal_value(self, data):
        if isinstance(data, list):
            return self.SEPARATOR.join([v.strip() for v in data])
        elif isinstance(data, str):
            return data.strip()
        raise serializers.ValidationError("Formato inválido — esperado lista de strings.")

class UserSerializer(serializers.ModelSerializer):
    autocuidado = MultiSelectFieldSerializer()
    doencasCronicas = MultiSelectFieldSerializer()
    vacinacao = MultiSelectFieldSerializer()
    atividadesDomesticas = MultiSelectFieldSerializer()
    atividadesSociaisLazer = MultiSelectFieldSerializer()
    mobilidade = MultiSelectFieldSerializer()
    funcoesCognitivas = MultiSelectFieldSerializer()
    atividadesSociais = MultiSelectFieldSerializer()
    atividadesLazer = MultiSelectFieldSerializer()
    atividadesCulturais = MultiSelectFieldSerializer()
    atividadesFisicasRecreativas = MultiSelectFieldSerializer()
    atividadesFamiliares = MultiSelectFieldSerializer()
    atividadesVoluntariado = MultiSelectFieldSerializer()

    class Meta:
        model = User
        fields = '__all__'

class AdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adm
        fields = '__all__'
