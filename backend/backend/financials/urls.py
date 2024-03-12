from django.urls import path
from .views import (
    InvoiceListCreateAPIView, InvoiceRetrieveUpdateDestroyAPIView,
    PaymentListCreateAPIView, PaymentRetrieveUpdateDestroyAPIView,
    ExpenseListCreateView, ExpenseRetrieveUpdateDestroyView,
    TenantStatementListAPIView, RunningBalanceListAPIView
)

urlpatterns = [
    # invoices urls
    path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/',
         InvoiceRetrieveUpdateDestroyAPIView.as_view(), name='invoice-detail'),

    # payment urls
    path('payments/', PaymentListCreateAPIView.as_view(),
         name='payment-list-create'),
    path('payments/<int:pk>/',
         PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),

    path('tenant-statements/', TenantStatementListAPIView.as_view(),
         name='tenant-statements-list'),

    path('running-balances/', RunningBalanceListAPIView.as_view(),
         name='running_balances_list'),


    # expenses urls
    # List and create expenses
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroyView.as_view(),
         name='expense-detail'),

]
