from operator import methodcaller
import re
from turtle import title
from unicodedata import name
from rest_framework.serializers import (
    SerializerMethodField,
    Serializer,
    DateTimeField,
    CharField,
    ImageField,
    IntegerField,
    DecimalField,
)
from stocksmarket.models import (
    Transaction,
    Holding,
    Account
)

from auths.models import CustomUser

# For converting QuerySet to JSON files


class UserSerializer(Serializer):

    id = IntegerField(read_only=True)
    user_name = CharField(read_only=True)
    

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'user_name',
        )

class AccountSerializer(Serializer):

    user = UserSerializer(read_only=True)
    id = IntegerField(read_only=True)
    account = account = DecimalField(required=False, max_digits=20, decimal_places=2)

    class Meta:
        model = Account
        fields = (
            'id',
            'account'
        )

    def create(self, validated_data):
        return Account.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.account = validated_data.get("account", instance.account)
        instance.save()
        return instance

class TransactionSerializer(Serializer):
    """TransactionUserSerializer."""
    user = UserSerializer(read_only=True)
    id = IntegerField(read_only=True)
    title = CharField(required=True)
    price_per_share = DecimalField(required=True, max_digits=20, decimal_places=2)
    total_price = DecimalField(required=True, max_digits=20, decimal_places=2)
    action = CharField(required=True)
    symbol = CharField(required=True)
    quantity = IntegerField(required=True)
    datetime_created = DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S")
    datetime_updated = DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S")
    datetime_deleted = DateTimeField(required=False, format="%Y-%m-%dT%H:%M:%S")


    class Meta:
        model = Transaction
        fields = (
            'user',
            'id',
            'title',
            'price_per_share',
            'total_price',
            'action',
            'symbol',
            'quantity',
            'datetime_created',
            'datetime_updated',
            'datetime_deleted',
        )

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price_per_share = validated_data.get("price_per_share", instance.price_per_share)
        instance.total_price = validated_data.get("total_price", instance.total_price)
        instance.action = validated_data.get("action", instance.action)
        instance.symbol = validated_data.get("symbol", instance.symbol)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.datetime_updated = validated_data.get("datetime_updated", instance.datetime_updated)
        instance.save()
        return instance
        
class HoldingSerializer(Serializer):
    """HoldingUserSerializer."""
    user = UserSerializer(read_only=True)
    id = IntegerField(read_only=True)
    title = CharField(required=True)
    price_per_share = DecimalField(required=True, max_digits=20, decimal_places=2)
    total_price = DecimalField(required=True, max_digits=20, decimal_places=2)
    symbol = CharField(required=True)
    quantity = IntegerField(required=True)
    datetime_created = DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S")
    datetime_updated = DateTimeField(read_only=True, format="%Y-%m-%dT%H:%M:%S")
    datetime_deleted = DateTimeField(required=False, format="%Y-%m-%dT%H:%M:%S")


    class Meta:
        model = Holding
        fields = (
            'user',
            'id',
            'title',
            'price_per_share',
            'total_price',
            'symbol',
            'quantity',
            'datetime_created',
            'datetime_updated',
            'datetime_deleted',
        )

    def create(self, validated_data):
        return Holding.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price_per_share = validated_data.get("price_per_share", instance.price_per_share)
        instance.total_price = validated_data.get("total_price", instance.total_price)
        instance.symbol = validated_data.get("symbol", instance.symbol)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.datetime_updated = validated_data.get("datetime_updated", instance.datetime_updated)
        instance.save()
        return instance