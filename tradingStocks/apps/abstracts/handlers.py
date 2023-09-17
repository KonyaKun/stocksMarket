# Обработка валидированных запросов и возвратить ответ в HTML
# Нужен для авторизации 
from typing import (
    Optional,
)
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from abstracts.mixins import HttpResponseMixin

# для mixin.py
class ViewHandler(HttpResponseMixin):
    """Handler for validating request and generating response."""
    'для обработки запроса и генерации ответа'

    def get_validated_response( # Проверка зашел ли пользователь на сайт со своего логина
        self,
        request: WSGIRequest
    ) -> Optional[HttpResponse]:
        """Get validated response."""

        if request.user.is_authenticated:
            return None

        return self.get_http_response(
            request,
            '../login/index.html'
        )