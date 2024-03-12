from django.db import models

# Create your models here.


class Property(models.Model):
    RENT_PENALTY_TYPE_CHOICES = (
        ('fixed', 'Fixed Amount'),
        ('percentage', 'Percentage'),
    )

    name = models.CharField(max_length=255)
    number_of_units = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    water_rate = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    electricity_rate = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    rent_penalty_type = models.CharField(
        max_length=10, choices=RENT_PENALTY_TYPE_CHOICES, blank=True, null=True)
    rent_penalty_amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    rent_penalty_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    # mpesa paybill
    tax_rate = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    management_fee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    street_name = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# other recurring bills


class PropertyOtherRecurringBill(models.Model):
    WATER = 'water'
    ELECTRICITY = 'electricity'
    GARBAGE = 'garbage'
    SECURITY = 'security'
    INTERNET = 'internet'
    CLEANING = 'cleaning'
    SERVICE = 'service'
    PARKING_FEE = 'parking fee'
    VAT = 'VAT'

    BILL_TYPE_CHOICES = [
        (WATER, 'Water'),
        (ELECTRICITY, 'Electricity'),
        (GARBAGE, 'Garbage'),
        (SECURITY, 'Security'),
        (INTERNET, 'Internet'),
        (CLEANING, 'Cleaning'),
        (SERVICE, 'Service'),
        (PARKING_FEE, 'Parking Fee'),
        (VAT, 'VAT'),
    ]

    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE, related_name='propertyrecurringbill')
    bill_type = models.CharField(
        max_length=100, choices=BILL_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_bill_type_display()} - {self.amount}"

# properties_app/models.py


class Unit(models.Model):
    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE, related_name='units')
    unit_id_or_name = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    occupied = models.BooleanField(default=False)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                   blank=True, help_text='Enter as percentage (e.g., 10.50 for 10.50%)')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.property.name} - {self.unit_id_or_name}"


class UnitOtherRecurringBill(models.Model):
    WATER = 'water'
    ELECTRICITY = 'electricity'
    GARBAGE = 'garbage'
    SECURITY = 'security'
    INTERNET = 'internet'
    CLEANING = 'cleaning'
    SERVICE = 'service'
    PARKING_FEE = 'parking fee'
    VAT = 'VAT'

    BILL_TYPE_CHOICES = [
        (WATER, 'Water'),
        (ELECTRICITY, 'Electricity'),
        (GARBAGE, 'Garbage'),
        (SECURITY, 'Security'),
        (INTERNET, 'Internet'),
        (CLEANING, 'Cleaning'),
        (SERVICE, 'Service'),
        (PARKING_FEE, 'Parking Fee'),
        (VAT, 'VAT'),
    ]

    unit = models.ForeignKey(
        'Unit', on_delete=models.CASCADE, related_name='unitrecurringbill')
    bill_type = models.CharField(
        max_length=100, choices=BILL_TYPE_CHOICES, default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_bill_type_display()} - {self.amount}"


class Utilities(models.Model):
    WATER = 'Water'
    ELECTRICITY = 'Electricity'
    GARBAGE = 'Garbage'
    SECURITY = 'Security'
    INTERNET = 'Internet'
    CLEANING = 'Cleaning'
    SERVICE = 'Service'
    PARKING = 'Parking'

    UTILITY_ITEM_CHOICES = [
        (WATER, 'Water'),
        (ELECTRICITY, 'Electricity'),
        (GARBAGE, 'Garbage'),
        (SECURITY, 'Security'),
        (INTERNET, 'Internet'),
        (CLEANING, 'Cleaning'),
        (SERVICE, 'Service'),
        (PARKING, 'Parking'),
    ]

    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]

    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE, related_name='utilities')
    unit = models.ForeignKey(
        'Unit', on_delete=models.CASCADE, related_name='utilities')
    utility_item = models.CharField(
        max_length=100, choices=UTILITY_ITEM_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    previous_reading = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    is_variable = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.utility_item in [self.WATER, self.ELECTRICITY]:
                # Get the latest utility instance for the same property, unit, and utility item
                latest_utility = Utilities.objects.filter(
                    property=self.property,
                    unit=self.unit,
                    utility_item=self.utility_item,
                    is_variable=self.is_variable  # Filter by variable or fixed utilities
                ).order_by('-id').first()

                if latest_utility:
                    self.previous_reading = latest_utility.current_reading
        super().save(*args, **kwargs)


class Maintenance(models.Model):
    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE, related_name='maintenance')
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE,
                             related_name='maintenance', null=True, blank=True)
    status = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    short_description = models.TextField(null=True, blank=True)
    image_upload = models.ImageField(
        upload_to='maintenance_images/', null=True, blank=True)
    expense_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.property.name} - {self.unit.unit_id_or_name} - {self.category}"
