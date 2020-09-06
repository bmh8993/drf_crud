from rest_framework import generics, mixins
from rest_framework import permissions

from board.models import Board
from .serializers import BoardSerializer
from .pagination import SmallSetPagination
from .permissions import IsWriterOrReadOnly


class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    pagination_class = SmallSetPagination


class BoardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsWriterOrReadOnly]


