from django.db import models
from core.models import Property, Unit
from tenant.models import Tenant
from core.models import CustomUser
from django.utils import timezone

# Create your models here.


class Invoice(models.Model):
    INVOICE_STATUS_CHOICES = (
        ('open', 'Open'),
        ('draft', 'Draft'),
        ('credit-note', 'Credit Note'),
    )

    ITEM_NAME_CHOICES = (
        ('rent', 'Rent'),
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('garbage', 'Garbage'),
        ('security', 'Security'),
        ('internet', 'Internet'),
        ('cleaning', 'Cleaning'),
        ('service', 'Service'),
        ('opening_balance', 'Opening Balance'),
        ('parking_fee', 'Parking Fee'),
        ('vat', 'VAT'),
        ('other', 'Other'),
        ('rent_deposit', 'Rent Deposit'),
        ('water_deposit', 'Water Deposit'),
        ('electricity_deposit', 'Electricity Deposit'),
        ('contract_charges', 'Contract Charges'),
        ('other_deposit', 'Other Deposit'),
    )

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='invoices')
    tenant = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, related_name='invoices')
    invoice_date = models.DateField()
    invoice_status = models.CharField(
        max_length=20, choices=INVOICE_STATUS_CHOICES)
    item_name = models.CharField(
        max_length=100, choices=ITEM_NAME_CHOICES, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_invoices')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Invoice #{self.id} - {self.property.name} - {self.tenant.first_name} {self.tenant.last_name}"


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    )

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='payments')
    tenant = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, related_name='payments')
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bank_transaction_id = models.CharField(
        max_length=100, blank=True, null=True)
    file_upload = models.FileField(
        upload_to='payment_receipts/', blank=True, null=True)

    # Timestamp when the payment was created
    created_at = models.DateTimeField(default=timezone.now)
    # Reference to the user who created the payment
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.property.name} - {self.tenant.first_name} {self.tenant.last_name}"


class TenantStatement(models.Model):
    transaction_date = models.DateField()
    item = models.CharField(max_length=100, blank=True, null=True)
    money_due = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    money_paid = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    running_balance = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tenant = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, related_name='statements')
    payment = models.OneToOneField(
        'Payment', on_delete=models.CASCADE, blank=True, null=True, related_name='tenant_statement')
    invoice = models.OneToOneField(
        Invoice, on_delete=models.CASCADE, blank=True, null=True, related_name='tenant_statement')
    # Timestamp when the statement was created
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Statement #{self.item}"


class RunningBalance(models.Model):
    tenant = models.OneToOneField(
        Tenant, on_delete=models.CASCADE, related_name='running_balance')
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name='Current Balance')

    def __str__(self):
        return f"Running Balance for {self.tenant.first_name} {self.tenant.last_name}: {self.balance}"


class Expense(models.Model):
    EXPENSE_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    )

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='expenses')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,
                             null=True, blank=True, related_name='unit_expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    expense_category = models.CharField(max_length=100)
    expense_date = models.DateField()
    status = models.CharField(max_length=20, choices=EXPENSE_STATUS_CHOICES)
    notes = models.TextField(blank=True, null=True)
    file_upload = models.FileField(
        upload_to='property_expenses/', blank=True, null=True)

    def __str__(self):
        return f"Expense #{self.id} - {self.property.name} - {self.expense_category}"
