from rest_framework import serializers
from atracoes.models import Atracoes


class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracoes
        fields = ['codigo', 'nome', 'idade_minima', 'ativo']
