from typing import Any
from rest_framework.permissions import BasePermission
from rest_framework.request import Request as DRF_Request


class CompanyPermission(BasePermission):

    def __init__(self) -> None:
        self._admin: bool = False
        self._user: bool = False

    def _initialize_permissions(self, request: DRF_Request) -> None:
        self._user = (
            request.user and
            request.user.is_active
        )
        self._admin = self._user and (
            request.user.is_staff and
            request.user.is_superuser
        )
    # has_object_permission можно запретить смотреть определенныей объект
    def has_permission(
        self,
        request: DRF_Request,
        view,
    ) -> bool:
        """Has permissions."""

        self._initialize_permissions(
            request
        )
        
        if view.action in (
            'list',
            'retrieve',
        ):
            return self._user

        if view.action in (
            'create',
            'partial_update',
            'update',
            'destroy',
        ):
            return self._admin

        return False