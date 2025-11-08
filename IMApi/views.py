from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Incident
from .serializers import (
    IncidentSerializer,
    IncidentCreateSerializer,
    IncidentUpdateSerializer
)


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_serializer_class(self):
        if self.action == 'create':
            return IncidentCreateSerializer
        elif self.action == 'update_status':
            return IncidentUpdateSerializer
        return IncidentSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            incident = serializer.save()
            return Response(
                IncidentSerializer(incident).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        try:
            incident = self.get_object()
        except Incident.DoesNotExist:
            return Response(
                {'error': 'Инцидент не найден'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(incident, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(IncidentSerializer(incident).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)