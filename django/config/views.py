from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    operation_summary='Get Resources',
    operation_description='Lorem ipsum dolor sit amet, ... (long description)',
    manual_parameters=[
        openapi.Parameter('parameter_a', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(
            None,
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'status': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='Data response',
                    ),
                },
                required=['status'],
            )
        )
    },
)
@api_view(['GET'])
def resources(*_):
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)