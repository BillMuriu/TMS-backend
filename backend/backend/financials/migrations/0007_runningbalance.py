# Generated by Django 5.0.1 on 2024-02-15 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0006_tenantstatement'),
        ('tenant', '0005_delete_tenantstatement'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunningBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Current Balance')),
                ('tenant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='running_balance', to='tenant.tenant')),
            ],
        ),
    ]
