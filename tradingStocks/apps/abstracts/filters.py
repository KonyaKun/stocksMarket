# Один из фильтров в Юзерах adminazavr
from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.contrib.admin import SimpleListFilter
from django.db.models import QuerySet


class CommonStateFilter(SimpleListFilter):
    title: str = 'Мильтр'
    parameter_name: str = 'stocks'

    def lookups( # то что в фильтрах показано
        self,
        request: WSGIRequest,
        model_admin: Any
    ) -> list:


        return [
            ('get_deleted', 'Удаленные'),
            ('get_not_deleted', 'Неудаленные'),
        ]

    def queryset( # после выборя работают условия
        self,
        request: WSGIRequest,
        queryset: QuerySet
    ) -> QuerySet:
        """QuerySet."""

        if self.value() == 'get_deleted':
            return queryset.filter(datetime_deleted__isnull=False)

        if self.value() == 'get_not_deleted':
            return queryset.filter(datetime_deleted__isnull=True)