from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import (Property,
                     Unit,
                     PropertyOtherRecurringBill,
                     Utilities,
                     UnitOtherRecurringBill,
                     Maintenance
                     )
from financials.serializers import ExpenseSerializer, InvoiceSerializer
from tenant.serializers import TenantSerializer


class UtilitiesSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    tenant = serializers.SerializerMethodField()
    property_name = serializers.CharField(
        source='property.name', read_only=True)
    unit_id_or_name = serializers.CharField(
        source='unit.unit_id_or_name', read_only=True)

    class Meta:
        model = Utilities
        fields = '__all__'

    def get_tenant(self, obj):
        unit = obj.unit
        if unit:
            # Assuming there can be multiple tenants over time
            tenant = unit.tenant_set.first()
            if tenant:
                return TenantSerializer(tenant).data
        return None


class UnitSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(
        source='property.name', read_only=True)
    utilities = UtilitiesSerializer(many=True, read_only=True)
    tenant = TenantSerializer(source='tenant_set', many=True, read_only=True)

    class Meta:
        model = Unit
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    units = UnitSerializer(many=True, read_only=True)
    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

    def get_url(self, obj):
        # return f"/api/v2/products/{obj.pk}/"
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse("property-detail", kwargs={"pk": obj.pk}, request=request)


class MaintenanceSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(
        source='property.name', read_only=True)
    unit_id_or_name = serializers.CharField(
        source='unit.unit_id_or_name', read_only=True)

    class Meta:
        model = Maintenance
        fields = '__all__'


class PropertyOtherRecurringBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyOtherRecurringBill
        fields = '__all__'


class UnitOtherRecurringBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOtherRecurringBill
        fields = '__all__'
