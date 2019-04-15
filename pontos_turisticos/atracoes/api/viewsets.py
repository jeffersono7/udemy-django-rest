from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #
    # def get_queryset(self):
    #     return Atracao.objects.all()

    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('nome', 'descricao')
