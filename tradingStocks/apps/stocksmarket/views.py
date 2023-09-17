# Вюшка готов и работает исправно
from typing import Optional
from datetime import datetime
from functools import partial

from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator
)
from abstracts.mixins import (
    JsonResponseMixin,
)
from stocksmarket.models import Transaction, Holding, Account # MODELS
from stocksmarket.serializers import (
    TransactionSerializer,
    HoldingSerializer,
    AccountSerializer
)

from stocksmarket.permissions import (
    CompanyPermission,
)

from rest_framework.parsers import (
    MultiPartParser, 
    FormParser,
    JSONParser
)


class TransactionViewSet(JsonResponseMixin, ViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    permission_classes: tuple = (
        AllowAny,
    )

 
    queryset: QuerySet[Transaction] = \
        Transaction.objects.get_not_deleted() 
    
    
    def get_queryset(self) -> QuerySet[Transaction]:   #get_queryset
        user = self.request.user.id
        return self.queryset.filter(
            user=user
        ) # email без super_user 

    @action( # дополнительный метод гет
        methods=['get'],
        detail=False,
        url_path='list_2',
        permission_classes=(
            CompanyPermission,
        )
    )


    def list_2(self, request: DRF_Request) -> DRF_Response:

        paginator: AbstractLimitOffsetPaginator = \
            AbstractLimitOffsetPaginator()

        objects: list = paginator.paginate_queryset( # из paginator он знает сколько обьектов ему надо, и вытаскиавает эти данные из БД
            self.get_queryset(),
            request
        )

        serializer: TransactionSerializer = \
            TransactionSerializer(
                objects,
                many=True
            )
        
        return self.get_json_response(
            serializer.data,
            paginator
        )
    
    def list(self, request: DRF_Request) -> DRF_Response:

        paginator: AbstractPageNumberPaginator = \
            AbstractPageNumberPaginator()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        
        print(objects)
        
        serializer: TransactionSerializer = \
            TransactionSerializer(
                objects,
                many=True
            )
        print(serializer)
        return self.get_json_response(
            serializer.data,
            paginator
        )
    
    def create(self, request: DRF_Request) -> DRF_Response:
        
        serializer: TransactionSerializer = \
            TransactionSerializer(
                data=request.data
            )
        print('ЕЩЁ НЕ ЗАШЕЛ')

        if serializer.is_valid(raise_exception=True):
            print("ЗАШЕЛ")
            serializer.save(user=self.request.user)
            return self.get_json_response(
                    {'data': f'{serializer.validated_data} are created'}
            )
        
        return DRF_Response({'data': 'Method Create'})

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод единичного элемента по ID
        transaction: Optional[Transaction] = None
        try:
            transaction: Transaction = self.get_queryset().get(id=pk)  # дает человека по айди
        except Transaction.DoesNotExist:
            return DRF_Response({'data': 'Не нашел пользователя'})
        
        serializer: TransactionSerializer = \
            TransactionSerializer(
                transaction
            )

        return DRF_Response({'response': serializer.data})
    
    def partial_update(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response:  # Метод обновление одного или более полей по ID
        if not pk:
            return DRF_Response({"error": "Method Partial update not allowed"})

        try:
            instance = Transaction.objects.get(pk=pk)
        except:
            return DRF_Response({"error": "Object does not exist"})

        serializer = TransactionSerializer(data=request.data, instance=instance, partial=True) # data те данные которые нужно поменять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return DRF_Response({"post": serializer.data})

    #PUT
    def update(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response: # Метод обновление целых данных по ID
    
        if not pk:
            return DRF_Response({"error": "Method Update not allowed"})

        try:
            instance = Transaction.objects.get(pk=pk)
        except:
            return DRF_Response({"error": "Object does not exist"})

        serializer = TransactionSerializer(data=request.data, instance=instance) # data те данные которые нужно поменять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return DRF_Response({"post": serializer.data})

    # DELETE
    def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод удаление

        transaction: Optional[Transaction] = None
        try:
            transaction: Transaction = self.get_queryset().get(id=pk) # ищет айди для удаление 
        except Transaction.DoesNotExist:
            return DRF_Response(
                {'data': f'Объект с ID: {pk} не найден'}   # если не нашел 
            )
        transaction.datetime_deleted = datetime.now()
        transaction.save(
            update_fields=['datetime_deleted'] # обновляет в базе данных только это поле
        )
        return DRF_Response({'data': f'Method {transaction.id} удален'})


class HoldingViewSet(JsonResponseMixin, ViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    permission_classes: tuple = (
        AllowAny,
    )
    
    queryset: QuerySet[Holding] = \
        Holding.objects.get_not_deleted()
        
    def get_queryset(self) -> QuerySet[Holding]:   #get_queryset
        user = self.request.user.id
        return self.queryset.filter(
            user=user
        ) # email без super_user 


    @action( # дополнительный метод гет
        methods=['get'],
        detail=False,
        url_path='list_2',
        permission_classes=(
            IsAdminUser,
        )
    )


    def list_2(self, request: DRF_Request) -> DRF_Response:

        paginator: AbstractLimitOffsetPaginator = \
            AbstractLimitOffsetPaginator()

        objects: list = paginator.paginate_queryset( # из paginator он знает сколько обьектов ему надо, и вытаскиавает эти данные из БД
            self.get_queryset(),
            request
        )
        serializer: HoldingSerializer = \
            HoldingSerializer(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )
    
    def list(self, request: DRF_Request) -> DRF_Response:

        paginator: AbstractPageNumberPaginator = \
            AbstractPageNumberPaginator()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: HoldingSerializer = \
            HoldingSerializer(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )
    
    def create(self, request: DRF_Request) -> DRF_Response:
        
        serializer: HoldingSerializer = \
            HoldingSerializer(
                data=request.data
            )
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print("ЗАШЕЛ")
            serializer.save(user=self.request.user)
            return self.get_json_response(
                    {'data': f'{serializer.validated_data} are created'}
            )
        
        return DRF_Response({'data': 'Method Create'})

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод единичного элемента по ID
        holding: Optional[Holding] = None
        try:
            holding: Holding = self.get_queryset().get(id=pk)  # дает человека по айди
        except Holding.DoesNotExist:
            return DRF_Response({'data': 'Не нашел пользователя'})
        
        serializer: HoldingSerializer = \
            HoldingSerializer(
                holding
            )

        return DRF_Response({'response': serializer.data})
    
    def partial_update(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response:  # Метод обновление одного или более полей по ID
        if not pk:
            return DRF_Response({"error": "Method Partial update not allowed"})

        try:
            instance = Holding.objects.get(pk=pk)
        except:
            return DRF_Response({"error": "Object does not exist"})

        serializer = HoldingSerializer(data=request.data, instance=instance, partial=True) # data те данные которые нужно поменять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return DRF_Response({"post": serializer.data})

    #PUT
    def update(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response: # Метод обновление целых данных по ID
    
        if not pk:
            return DRF_Response({"error": "Method Update not allowed"})

        try:
            instance = Holding.objects.get(pk=pk)
        except:
            return DRF_Response({"error": "Object does not exist"})

        serializer = HoldingSerializer(data=request.data, instance=instance) # data те данные которые нужно поменять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return DRF_Response({"post": serializer.data})

    # DESTROY
    def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод удаление

        holding: Optional[Holding] = None
        try:
            holding: Holding = self.get_queryset().get(id=pk) # ищет айди для удаление 
        except Holding.DoesNotExist:
            return DRF_Response(
                {'data': f'Объект с ID: {pk} не найден'}   # если не нашел 
            )
        holding.datetime_deleted = datetime.now()
        holding.save(
            update_fields=['datetime_deleted'] # обновляет в базе данных только это поле
        )
        return DRF_Response({'data': f'Method {holding.id} удален'})


class AccountViewSet(JsonResponseMixin, ViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    permission_classes: tuple = (
        AllowAny,
    )
    
    queryset: QuerySet[Account] = \
        Account.objects.get_not_deleted()
        
    def get_queryset(self) -> QuerySet[Account]:   #get_queryset
        user = self.request.user.id
        return self.queryset.filter(
            user=user
        ) # email без super_user 


    @action( # дополнительный метод гет
        methods=['get'],
        detail=False,
        url_path='list_2',
        permission_classes=(
            IsAdminUser,
        )
    )


    def list_2(self, request: DRF_Request) -> DRF_Response:

        paginator: AbstractLimitOffsetPaginator = \
            AbstractLimitOffsetPaginator()

        objects: list = paginator.paginate_queryset( # из paginator он знает сколько обьектов ему надо, и вытаскиавает эти данные из БД
            self.get_queryset(),
            request
        )
        serializer: AccountSerializer = \
            AccountSerializer(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )
    
    def list(self, request: DRF_Request) -> DRF_Response:

        paginator: AbstractPageNumberPaginator = \
            AbstractPageNumberPaginator()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: AccountSerializer = \
            AccountSerializer(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )
    
    def create(self, request: DRF_Request) -> DRF_Response:
        
        serializer: AccountSerializer = \
            AccountSerializer(
                data=request.data
            )
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print("ЗАШЕЛ")
            serializer.save(user=self.request.user)
            return self.get_json_response(
                    {'data': f'{serializer.validated_data} are created'}
            )
        
        return DRF_Response({'data': 'Method Create'})

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод единичного элемента по ID
        account: Optional[Account] = None
        try:
            account: Account = self.get_queryset().get(id=pk)  # дает человека по айди
        except Account.DoesNotExist:
            return DRF_Response({'data': 'Не нашел пользователя'})
        
        serializer: AccountSerializer = \
            AccountSerializer(
                account
            )

        return DRF_Response({'response': serializer.data})
    
    def partial_update(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response:  # Метод обновление одного или более полей по ID
        if not pk:
            return DRF_Response({"error": "Method Partial update not allowed"})

        try:
            instance = Account.objects.get(pk=pk)
        except:
            return DRF_Response({"error": "Object does not exist"})

        serializer = AccountSerializer(data=request.data, instance=instance, partial=True) # data те данные которые нужно поменять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return DRF_Response({"post": serializer.data})

    #PUT
    def update(
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response: # Метод обновление целых данных по ID
    
        if not pk:
            return DRF_Response({"error": "Method Update not allowed"})

        try:
            instance = Account.objects.get(pk=pk)
        except:
            return DRF_Response({"error": "Object does not exist"})

        serializer = AccountSerializer(data=request.data, instance=instance) # data те данные которые нужно поменять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return DRF_Response({"post": serializer.data})

    # DELETE
    def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод удаление

        account: Optional[Account] = None
        try:
            account: Account = self.get_queryset().get(id=pk) # ищет айди для удаление 
        except Account.DoesNotExist:
            return DRF_Response(
                {'data': f'Объект с ID: {pk} не найден'}   # если не нашел 
            )
        account.datetime_deleted = datetime.now()
        account.save(
            update_fields=['datetime_deleted'] # обновляет в базе данных только это поле
        )
        return DRF_Response({'data': f'Method {account.id} удален'})