from typing import Optional

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest
from abstracts.filters import CommonStateFilter

from auths.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
 
    fieldsets = (   # для отражение полей в настройках пользователя
        ('Information', {
            'fields':(
                'user_name',
                'first_name',
                'last_name',
                'email',
                'image_url',
                'password',
                'date_joined',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),
    )


    add_fieldsets = (  # для добавление пользователя
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'user_name',
                'first_name',
                'last_name',
                'email',
                'image_url',
                'password1',
                'password2',
                'is_active',
            ),
        }),
    )

    search_fields = (  # поиск по емайл
        'email',
    )

    readonly_fields = ( # поля которые не сможешь изменить 
        'date_joined',
        'is_superuser',
        'is_staff',
        'is_active',
    )

    list_display = (  # Отражение полей в списке пользователей
        'user_name',
        'first_name',
        'last_name',
        'email',
        'password',
        'date_joined',
        'is_staff',
        'is_active',
    )

    list_filter = ( 
        'email',
        'is_superuser',
        'is_staff',
        'is_active',
        CommonStateFilter

    )

    ordering = ( # По порядку по имени
        'user_name',
    )


admin.site.register(
    CustomUser, CustomUserAdmin
)

