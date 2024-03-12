# Generated by Django 5.0.1 on 2024-02-15 16:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_customuser_alter_landlord_user_and_more'),
        ('financials', '0007_runningbalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.customuser'),
        ),
    ]