from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})
        # return Response(PontoTuristico.objects.all())

    def create(self, request, *args, **kwargs):
        return Response({ 'Hello': request.data['nome'] })

    def destroy(self, request, *args, **kwargs):
        return Response()

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get'], detail=True)
    def denunciar(self, request, *args, **kwargs):
        pass