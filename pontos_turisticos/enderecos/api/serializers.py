from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EnderecosSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'linha1',
            'cidade',
            'estado',
            'pais'
        )