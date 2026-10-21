from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    @action(detail=False, methods=['get'], url_path='autor/(?P<nome>[^/.]+)')
    def por_autor(self, request, nome=None):
        livros = self.queryset.filter(autor__icontains=nome)
        serializer = self.get_serializer(livros, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='ano/(?P<ano>[0-9]+)')
    def por_ano(self, request, ano=None):
        livros = self.queryset.filter(publicado_em__year=ano)
        serializer = self.get_serializer(livros, many=True)
        return Response(serializer.data)