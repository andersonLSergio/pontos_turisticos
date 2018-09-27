from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        # prepares the statement to get all from the database (lazyload)
        # lazyload doesn't retrieve data itself, it only prepares the statement
        # so it's okay to keep it here
        queryset = PontoTuristico.objects.all()

        if id:
            # if it's given an id (primary key), we want to get just one occurency from the db
            queryset = PontoTuristico.objects.filter(pk=id)
        
        if nome:
            # if it's given this param, the filter is applied
            queryset = queryset.filter(nome=nome)

        if descricao:
            # if it's given this param, the filter is applied
            queryset = queryset.filter(descricao=descricao)

        # this is when the data is actually retrieved with all the rules applied earlier
        return queryset

    #GET ACTION
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    #POST ACTION
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    #DELETE ACTION
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    #GET ACTION FOR UNIC RESULT
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    #PUT ACTION
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    #PATCH ACTION
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass