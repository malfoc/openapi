from django.contrib import admin
from django.urls import path
from config import views
from rest_framework import permissions

# Se importa el package drf_yasg
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Se configuran los siguientes métodos para habilitar la documentación
schema_view = get_schema_view(
    openapi.Info(
        title="Mi Django API",
        default_version='v1.0.0',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('resources', views.resources, name="resources"),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
