from django.contrib import admin
from .models import TenantStatement, RunningBalance, Payment, Invoice

# Register your models here.
admin.site.register(TenantStatement)
admin.site.register(RunningBalance)
admin.site.register(Payment)
admin.site.register(Invoice)
