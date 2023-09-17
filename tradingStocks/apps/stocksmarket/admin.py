from calendar import c
from django.contrib import admin

from .models import Transaction, Holding, Account

class TransactionAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )


class HoldingAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

class AccountAdmin(admin.ModelAdmin):

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Holding, HoldingAdmin)
admin.site.register(Account, AccountAdmin)

admin.site.site_title = 'Админ панель сайта о акциях компании'
admin.site.site_header = 'Админ панель сайта о акциях компании'