from django.db import models
from core.models import Property, Unit
# Create your models here.


class Tenant(models.Model):

    RENT_PENALTY_TYPE_CHOICES = (
        ('fixed', 'Fixed Amount'),
        ('percentage', 'Percentage'),
    )

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    kra_tax_pin = models.CharField(max_length=20, blank=True, null=True)
    rent_penalty_type = models.CharField(
        max_length=10, choices=RENT_PENALTY_TYPE_CHOICES, blank=True, null=True)
    rent_penalty_amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    rent_penalty_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    move_in_date = models.DateField(blank=True, null=True)
    move_out_date = models.DateField(blank=True, null=True)
    other_phone_numbers = models.CharField(
        max_length=100, blank=True, null=True)
    lease_start_date = models.DateField(blank=True, null=True)
    lease_expiry_date = models.DateField(blank=True, null=True)
    lease_notes = models.TextField(blank=True, null=True)
    file_upload = models.FileField(
        upload_to='tenant_documents/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class RentDeposit(models.Model):
    RENT_DEPOSIT_CHOICES = (
        ('rent', 'Rent'),
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('service_charge', 'Service Charge'),
        ('other', 'Other'),
    )

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    deposit_type = models.CharField(
        max_length=50, choices=RENT_DEPOSIT_CHOICES)
    amount_paid = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    amount_returned = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.deposit_type
