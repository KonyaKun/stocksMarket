from typing import Optional
from datetime import datetime

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet
from abstracts.mixins import (
    JsonResponseMixin,
)
from abstracts.validators import APIValidator
from auths.models import CustomUser
from auths.serializers import CustomUserSerializer

from rest_framework.parsers import (
    MultiPartParser, 
    FormParser,
    JSONParser
)

class CustomUserViewSet(JsonResponseMixin, ViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    permission_classes: tuple = (AllowAny,) 

    queryset: QuerySet[CustomUser] = \
        CustomUser.objects.get_not_deleted() #  object не удаленные

    def get_queryset(self) -> QuerySet[CustomUser]:                        #get_queryset
        return self.queryset.filter(
            is_superuser=False
        ) # email без super_user

    @action(
        methods=['get'], 
        detail=False, 
        url_path='my_custom_endpoint', 
        permission_classes=(
            AllowAny, # разрешается любому пользователю применять post
        )
    ) # Метод post 
    def my_custom_endpoint(
        self, 
        request: DRF_Request, 
    ) -> DRF_Response:
        
        data: list = [
            user.id for user in self.get_queryset()
        ]
        return self.get_json_response(
            data
        )

    def list(self, request: DRF_Request) -> DRF_Response: # Метод Списка элементов
        
        serializer: CustomUserSerializer = \
            CustomUserSerializer(
                self.get_queryset(),
                many=True
            ) # дает словарь который мы преобразуем в ДЖСОН

        return self.get_json_response( # Внутри есть DRF_Response он та и хуярит ДЖСОН формат
            serializer.data
        )

    def create(self, request: DRF_Request) -> DRF_Response: # POST at the end of the list

        serializer: CustomUserSerializer = \
            CustomUserSerializer(
                data=request.data
            )
        if serializer.is_valid(raise_exception=True): # проверяет поля сериализатора
            serializer.save() # добавление новых данных в БД
            return self.get_json_response(
                f'Object {serializer.validated_data} is created'
            )

        return DRF_Response({'data': 'Method Auths Create'})

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод единичного элемента по GET ID 
        custom_user: Optional[CustomUser] = None
        try:
            custom_user: CustomUser = self.get_queryset().get(id=pk)  # дает человека по айди
        except CustomUser.DoesNotExist:
            return DRF_Response({'data': 'Не нашел пользователя'})
        
        serializer: CustomUserSerializer = \
            CustomUserSerializer(
                custom_user
            )

        return self.get_json_response(
            serializer.data
        )
    
    def partial_update( # Patch 
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response:  # Метод обновление одного или более полей по ID
        raise APIValidator(
            '\'PATCH\' метод не имплементирован',
            'warning',
            '403'
        )

    def update( # PUT
        self, 
        request: DRF_Request, 
        pk: int = 0
    ) -> DRF_Response: # Метод обновление целых данных по ID
        raise APIValidator(
            '\'PUT\' метод не имплементирован',
            'warning',
            '403'
        )

    def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response: # Метод удаление DELETE

        custom_user: Optional[CustomUser] = None
        try:
            custom_user: CustomUser = self.get_queryset().get(id=pk) # ищет айди для удаление 
        except CustomUser.DoesNotExist:
            return DRF_Response(
                {'data': f'Объект с ID: {pk} не найден'}   # если не нашел 
            )
        custom_user.datetime_deleted = datetime.now()
        custom_user.save(
            update_fields=['datetime_deleted'] # обновляет в базе данных только это поле
        )
        return self.get_json_response(
            f'Method {custom_user.id} удален'
        )
    
class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request=DRF_Request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return DRF_Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return DRF_Response(status=status.HTTP_400_BAD_REQUEST)