# Generated by Django 5.0.1 on 2024-01-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_propertyotherrecurringbill_bill_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitotherrecurringbill',
            name='bill_type',
            field=models.CharField(choices=[('water', 'Water'), ('electricity', 'Electricity'), ('garbage', 'Garbage'), ('security', 'Security'), ('internet', 'Internet'), ('cleaning', 'Cleaning'), ('service', 'Service'), ('parking fee', 'Parking Fee'), ('VAT', 'VAT')], max_length=100),
        ),
    ]
