from datetime import datetime
from django.db.models import (
    QuerySet,
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    PROTECT,
    CASCADE,
    ImageField,
)
from django.db import models
from auths.models import CustomUser

from abstracts.models import AbstractDateTime
    

class HoldingQuerySet(QuerySet):
    """Holding queryset."""

    def get_deleted(self) -> QuerySet['Holding']:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self) -> QuerySet['Holding']:
        return self.filter(
            datetime_deleted__isnull=True
        )
    
class Holding(AbstractDateTime):        
    user = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price_per_share = models.DecimalField(max_digits=20,decimal_places=2)
    total_price = models.DecimalField(max_digits=20,decimal_places=2)
    symbol = models.CharField(max_length=255)
    quantity = models.IntegerField()   
        
    objects = HoldingQuerySet().as_manager()

    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'
        ordering = ['id']

    def __str__(self):
        return self.title

class TransactionQuerySet(QuerySet):
    """Transaction queryset."""

    def get_deleted(self) -> QuerySet['Transaction']:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self) -> QuerySet['Transaction']:
        return self.filter(
            datetime_deleted__isnull=True
        )

class Transaction(AbstractDateTime):
    user = models.ForeignKey(CustomUser, related_name='user', blank=True, on_delete=models.CASCADE)
    title = CharField(
        verbose_name='Название',
        max_length=255
    ) # название компании

    price_per_share = models.DecimalField(max_digits=20,decimal_places=2) # Цена за одну акцию
    total_price = models.DecimalField(max_digits=20,decimal_places=2) # Общая сумма
    action = models.CharField(max_length=255) # BOUGHT/SOLD
    symbol = models.CharField(max_length=255)
    quantity = models.IntegerField()
   
    objects = TransactionQuerySet().as_manager()

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['id']

    def __str__(self):
        return self.title
    

class AccountQuerySet(QuerySet):
    """Transaction queryset."""

    def get_deleted(self) -> QuerySet['Account']:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self) -> QuerySet['Account']:
        return self.filter(
            datetime_deleted__isnull=True
        )

class Account(AbstractDateTime):
    user = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)
    account = models.DecimalField(blank=True, null=True, max_digits=20,decimal_places=2)

    objects = AccountQuerySet().as_manager()

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        ordering = ['id']

