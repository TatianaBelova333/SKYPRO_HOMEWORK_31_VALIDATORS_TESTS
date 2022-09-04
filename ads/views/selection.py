from rest_framework.permissions import IsAuthenticated
from ads.models import Selection
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.permissions import SelectionDeletePermission, SelectionUpdatePermission
from ads.serializers.selection import SelectionListSerializer, SelectionDetailSerializer, SelectionCreateSerializer, \
    SelectionDestroySerializer, SelectionUpdateSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionUpdatePermission]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDestroySerializer
    permission_classes = [IsAuthenticated, SelectionDeletePermission]
