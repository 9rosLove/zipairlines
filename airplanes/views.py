from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from airplanes.models import Airplane
from airplanes.pagination import AirplanePagination
from airplanes.serializers import AirplaneSerializer, AirplaneDetailSerializer


class AirplaneViewset(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = AirplanePagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["airplane_id", "passengers_count"]
    search_fields = ["airplane_id", ]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == "retrieve":
            serializer_class = AirplaneDetailSerializer
        return serializer_class

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "retrieve":
            queryset = queryset.select_related("created_by")
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
