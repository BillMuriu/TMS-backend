from django.contrib import admin
from .models import Property

# Define the admin class for the Property model


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_units', 'city',
                    'water_rate', 'electricity_rate', 'rent_penalty_type')
    # Add more customization as needed


# Register the Property model with its admin class
admin.site.register(Property, PropertyAdmin)
