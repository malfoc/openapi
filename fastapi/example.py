from fastapi import FastAPI, Response

# El framework FastAPI cuenta con la documentación openapi
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi

app = FastAPI()

# Se importa Pydantic para la configuración de los schemas
from pydantic import BaseModel, Field, constr

# Se pueden configura los schemas de respuesta y de peticiòn
class RequestSchema(BaseModel):
    parameter_a: constr(min_length=2, max_length=40)  # Constrained Str
    parameter_b: int = Field(..., gt=0, lt=150, description="user age(Human)")

class ResponseSchema(BaseModel):
    status: str

# Clase de ejemplo de un recurso
@app.get("/resources", response_model=ResponseSchema)
def get_resources(request:RequestSchema):
    """ 
    GET Resources (summary of this endpoint)

    Lorem ipsum dolor sit amet, ... (long description)
    """
    return {'status': 'ok'}

# Se configuran los siguientes métodos para habilitar la documentación
def custom_openapi():
    """
    Generar definición de OpenAPI personalizada
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mi FastAPI API",
        version="1.0.0",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@app.get("/docs", include_in_schema=False)
async def get_documentation():
    """
    Servir la documentación de la API con Swagger UI
    """
    openapi_schema = custom_openapi()
    return get_swagger_ui_html(
        openapi_schema=openapi_schema
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    """
    Servir la documentación de la API con Redoc
    """
    openapi_schema = custom_openapi()
    return get_redoc_html(
        openapi_schema=openapi_schema
    )

# Lectura de la documentación
# http://localhost:8000/swagger
# http://localhost:8000/redoc