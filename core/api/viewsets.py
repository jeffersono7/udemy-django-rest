from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    # queryset = PontoTuristico.objects.filter(aprovado=True)
    authentication_classes = (TokenAuthentication, )
    permission_classes = (DjangoModelPermissions, )

    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('nome', 'descricao', '^endereco__linha1')
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
        # return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
        # return Response({'teste': 123})
        # return Response(PontoTuristico.objects.all())

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
        # return Response({ 'Hello': request.data['nome'] })

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
        # return Response()

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
        # pass

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
        # pass

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
        # pass

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

    @action(methods=['post'], detail=True)
    def associar_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()

        return HttpResponse.status_code('200')
