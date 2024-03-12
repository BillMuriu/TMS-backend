from rest_framework import serializers
from .models import Invoice, Payment, Expense, TenantStatement, RunningBalance
# from tenant.serializers import TenantStatementSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(
        source='property.name', read_only=True)
    tenant_name = serializers.CharField(
        source='tenant.first_name', read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class RunningBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningBalance
        fields = '__all__'


class TenantStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantStatement
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(
        source='property.name', read_only=True)
    tenant_name = serializers.CharField(
        source='tenant.first_name', read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(
        source='property.name', read_only=True)
    unit_id_or_name = serializers.CharField(
        source='unit.unit_id_or_name', read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'
