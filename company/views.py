from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=False, methods=['delete'], url_path='delete-all')
    def delete_all(self, request):
        # Confirm deletion if necessary
        Company.objects.all().delete()
        return Response({'message': 'All companies deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
