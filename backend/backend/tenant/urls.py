from django.urls import path
from .views import (TenantListView,
                    TenantDetailView,
                    RentDepositListView,
                    RentDepositDetailView,
                    )

urlpatterns = [
    path('', TenantListView.as_view(), name='tenant-list'),
    path('<int:pk>/', TenantDetailView.as_view(), name='tenant-detail'),

    path('rent-deposits/', RentDepositListView.as_view(), name='rent-deposit-list'),
    path('rent-deposits/<int:pk>/', RentDepositDetailView.as_view(),
         name='rent-deposit-detail'),
]
