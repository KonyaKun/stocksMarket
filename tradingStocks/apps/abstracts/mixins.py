from typing import (
    Optional,
    Union,
)
from rest_framework.response import Response as DRF_Response

from django.core.handlers.wsgi import WSGIRequest
from django.template import (
    loader,
    backends,
)
from django.http import HttpResponse

from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)
# один для ДЖСОН респонса другой для ХТМЛ

class HttpResponseMixin: # Нужен будет для авторизации пользователя
    """Mixin for handling HTTP response rendering."""

    content_type: str = 'text/html'

    def get_http_response(
        self,
        request: WSGIRequest,
        template_name: str, # путь к странице логина и пароля
        context: dict = {}
    ) -> HttpResponse:
        """Get HTTP response."""

        template: backends.django.Template =\
            loader.get_template(
                template_name
            ) # загружает страницу по указанному пути и компилирует

        return HttpResponse( # возвращает от рендеренный уже со всеми данными из БД
            template.render(
                context,
                request
            ),
            content_type=self.content_type # для уточнения типа запроса
        )
        # NOTE: Alternative approach:
        #       from django.shortcuts import render
        #       return render(
        #           request,
        #           template_name='university/index.html',
        #           context=context
        #       )


class JsonResponseMixin:
    """Mixin for handling JSON response rendering."""

    def get_json_response(
        self,
        data: Union[dict, str], # либо словарь либо строка
        paginator: Optional[
            Union[
                AbstractLimitOffsetPaginator,
                AbstractPageNumberPaginator,
            ]
        ] = None # либо Юнион либо ничего
    ) -> DRF_Response:
        """Get JSON response."""

        response: Optional[DRF_Response] = None
        
        if paginator: # если один из пагинаторов вызывается во View то тут он пагинируется
            response = paginator.get_paginated_response(
                data
            )
            
        else:
            response = DRF_Response(
                {
                    'results': data,
                }
            )

        
        return response