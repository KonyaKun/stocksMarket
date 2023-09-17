from typing import Any
from apps.stocksmarket.views import TransactionViewSet, HoldingViewSet, AccountViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.auths.views import CustomUserViewSet, LogoutView

urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += [
        path('debug/', include('debug_toolbar.urls')),
    ]

# ---------------------------------------------------
# API-Endpoints
#


router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)

router.register(
    'auths',
    CustomUserViewSet, 
    basename='auths',
)

router.register(
    'transaction',
    TransactionViewSet, 
    basename='transaction',
)

router.register(
    'holding',
    HoldingViewSet, 
    basename='holding',
)

router.register(
    'account',
    AccountViewSet, 
    basename='account',
)

urlpatterns += [
    path(
        'api/v1/', 
        include(router.urls)
    ),
        path('api/v1/drf-auth', 
         include('rest_framework.urls')
    ),
    path(
        'api/v1/token/', 
        TokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'api/v1/token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),
    path(
        'api/v1/token/verify/', 
        TokenVerifyView.as_view(), 
        name='token_verify'
    ),
    path(
        'api/v1/logout',
        LogoutView.as_view(),
        name='logout',
    ),
]
