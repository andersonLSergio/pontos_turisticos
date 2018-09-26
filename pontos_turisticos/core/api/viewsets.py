from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    #GET ACTION
    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

    #POST ACTION
    def create(self, request, *args, **kwargs):
        return Response({'Hello': request.data['nome']})

    #DELETE ACTION
    def destroy(self, request, *args, **kwargs):
        pass

    #GET ACTION FOR UNIC RESULT
    def retrieve(self, request, *args, **kwargs):
        pass

    #PUT ACTION
    def update(self, request, *args, **kwargs):
        pass

    #PATCH ACTION
    def partial_update(self, request, *args, **kwargs):
        pass