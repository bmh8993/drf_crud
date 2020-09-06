from django.urls import path, include
from .views import BoardListCreateAPIView, BoardDetailAPIView

urlpatterns = [
    path('board/', BoardListCreateAPIView.as_view(), name='board-list'),
    path('board/<int:pk>/', BoardDetailAPIView.as_view(), name='board-detail'),
    # path('board/<int:pk>/update', BoardUpdateAPIView.as_view(), name='board-update'),
    # path('board/<int:pk>/delete', BoardDestroyAPIView.as_view(), name='board-delete'),
]
