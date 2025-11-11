from rest_framework import serializers
from .models import User, Adm
import json


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer do User com validação dos choices exatamente iguais ao front (opcoesFormulario.js).
    """

    class Meta:
        model = User
        fields = "__all__"

    # Choices idênticos aos do opcoesFormulario.js
    CHOICES = {
        "doencasCronicas": [
            "Hipertensão arterial",
            "Diabetes mellitus",
            "Doença cardíaca (ex.: infarto, angina, insuficiência cardíaca)",
            "AVC ou acidente isquêmico transitório",
            "Doença pulmonar crônica (ex.: asma, DPOC)",
            "Câncer (qualquer tipo)",
            "Doença renal crônica",
            "Depressão ou outro transtorno mental",
            "Outra",
            "Nenhuma dessas",
        ],
        "vacinacao": [
            "Gripe (influenza)",
            "Pneumocócica",
            "COVID-19 (reforço)",
        ],
        "autocuidado": [
            "Alimenta-se sozinho(a)",
            "Toma banho ou higiene pessoal",
            "Vai ao banheiro sozinho(a)",
            "Deita-se/levanta-se da cama ou cadeira",
            "Nenhuma dificuldade observada",
        ],
        "atividadesDomesticas": [
            "Prepara refeições",
            "Faz compras de alimentos ou itens de casa",
            "Lava roupas ou limpar a casa",
            "Controla as próprias finanças/pagar contas",
            "Usa telefone ou celular",
            "Nenhuma dificuldade observada",
        ],
        "atividadesSociaisLazer": [
            "Participa de atividades religiosas, culturais ou sociais",
            "Mantem hobbies ou passatempos (ex.: jardinagem, música, leitura)",
            "Sai de casa para lazer (ex.: visitas, cinema, encontros)",
            "Conversa/interage com amigos ou familiares",
            "Nenhuma dificuldade observada",
        ],
        "mobilidade": [
            "Caminha dentro de casa",
            "Caminha longas distâncias (mais de 400m)",
            "Sobe ou desce escadas",
            "Nenhuma dificuldade observada",
        ],
        "funcoesCognitivas": [
            "Lembra compromissos ou conversas recentes",
            "Encontra objetos pessoais",
            "Reconhece pessoas próximas",
            "Segue instruções simples",
            "Nenhuma dificuldade observada",
        ],
        "atividadesSociais": [
            "Conversar com amigos ou familiares",
            "Participar de grupos comunitários, associações ou clubes",
            "Participar de eventos sociais (festas, encontros, reuniões)",
            "Nenhuma dessas",
        ],
        "atividadesLazer": [
            "Ler livros, jornais ou revistas",
            "Assistir televisão, ouvir rádio, ouvir música",
            "Ir ao cinema, teatro ou shows",
            "Jogar cartas, dominó, jogos de tabuleiro ou eletrônicos",
            "Nenhuma dessas",
        ],
        "atividadesCulturais": [
            "Participar de cultos, missas ou grupos religiosos/espirituais",
            "Praticar meditação, oração ou atividades espirituais pessoais",
            "Participar de oficinas de arte, música ou dança",
            "Nenhuma dessas",
        ],
        "atividadesFisicasRecreativas": [
            "Caminhadas ou passeios ao ar livre",
            "Jardinagem, horta ou cuidados com plantas",
            "Exercícios em grupo (dança, hidroginástica, yoga)",
            "Esportes recreativos (futebol, vôlei, bocha, ciclismo, etc.)",
            "Nenhuma dessas",
        ],
        "atividadesFamiliares": [
            "Estar com filhos/netos",
            "Cuidar de familiares",
            "Preparar refeições e compartilhar momentos em família",
            "Reunir a família em datas especiais",
            "Nenhuma dessas",
        ],
        "atividadesVoluntariado": [
            "Ajudar vizinhos ou amigos",
            "Fazer trabalho voluntário em instituições",
            "Ensinar ou compartilhar conhecimentos com outras pessoas",
            "Nenhuma dessas",
        ],
    }

    # Validações simples
    def validate_idade(self, value):
        if value is None:
            return value
        if not isinstance(value, int):
            raise serializers.ValidationError("Idade deve ser um número inteiro.")
        if value < 0 or value > 120:
            raise serializers.ValidationError("A idade deve estar entre 0 e 120 anos.")
        return value

    def validate_rendaMensal(self, value):
        if value is None:
            return value
        if not isinstance(value, int):
            raise serializers.ValidationError("Renda mensal deve ser um número inteiro.")
        if value < 0:
            raise serializers.ValidationError("A renda mensal não pode ser negativa.")
        return value

    # Validação geral dos campos tipo lista / JSON
    def validate(self, attrs):
        for field, valid_list in self.CHOICES.items():
            label = field  # mantém o nome do campo para mensagens
            value = attrs.get(field, None)

            # permitir campo ausente ou vazio
            if value in [None, "", []]:
                attrs[field] = []
                continue

            # se veio como string JSON (ex: '["A","B"]'), tenta converter
            if isinstance(value, str):
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    raise serializers.ValidationError({
                        field: f"O campo '{label}' deve ser uma lista JSON válida (ex: ['A', 'B'])."
                    })

            # agora deve ser lista
            if not isinstance(value, list):
                raise serializers.ValidationError({
                    field: f"O campo '{label}' deve ser uma lista (array JSON)."
                })

            # cada item deve ser string e estar entre os choices do front
            cleaned = []
            for item in value:
                if not isinstance(item, str):
                    raise serializers.ValidationError({
                        field: f"Todos os itens de '{label}' devem ser textos (strings)."
                    })
                item_stripped = item.strip()
                if item_stripped == "":
                    continue  # ignora strings vazias
                if item_stripped not in valid_list:
                    # mensagem clara e em pt-BR
                    raise serializers.ValidationError({
                        field: f"'{item}' não é uma opção válida para '{label}'."
                    })
                cleaned.append(item_stripped)

            attrs[field] = cleaned

        return attrs


class AdmSerializer(serializers.ModelSerializer):
    """Serializer simples para Adm (sem nome/email/senha conforme solicitado)."""
    class Meta:
        model = Adm
        fields = "__all__"
