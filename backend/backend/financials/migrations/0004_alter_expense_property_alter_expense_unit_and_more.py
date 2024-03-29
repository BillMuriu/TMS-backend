# Generated by Django 5.0.1 on 2024-01-26 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0003_expense'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='property.property'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_expenses', to='property.unit'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='property.property'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='property.property'),
        ),
    ]
