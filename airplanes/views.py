from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer, AirplaneDetailSerializer


class AirplaneViewset(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == "retrieve":
            serializer_class = AirplaneDetailSerializer
        return serializer_class

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
