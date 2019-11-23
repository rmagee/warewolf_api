from django.contrib import admin
from warewolf_api import models


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )
    exclude = ['record_time',
     'event_time',
     'event_timezone_offset',
     ]
    readonly_fields = [
        'event_id'
    ]

def register_to_site(admin_site):
    admin_site.register(models.Transaction, TransactionAdmin)
