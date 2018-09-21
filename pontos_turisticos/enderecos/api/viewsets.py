from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecosSerializer


class EnderecoViewset(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer