from rest_framework import generics
from .models import Tenant, RentDeposit
from .serializers import TenantSerializer, RentDepositSerializer, TenantStatementSerializer
from django_filters.rest_framework import DjangoFilterBackend


'''
TENANT DEPOSIT CRUD
'''


class TenantListView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['property']


class TenantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


'''
RENT DEPOSIT CRUD
'''


class RentDepositListView(generics.ListCreateAPIView):
    queryset = RentDeposit.objects.all()
    serializer_class = RentDepositSerializer


class RentDepositDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentDeposit.objects.all()
    serializer_class = RentDepositSerializer
