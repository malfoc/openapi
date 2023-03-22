import falcon
import json

# El package SpecTree está diseñado para varios frameworks de python Flask | Falcon | Starlette
from spectree import SpecTree, Response

# Configurar una instancia de SpecTree
spec = SpecTree('falcon', title='My Falcon API', version='1.0', annotations=True)

# Se importa Pydantic para la configuración de los schemas
from pydantic import BaseModel, Field, constr

# Se pueden configura los schemas de respuesta y de peticiòn
class RequestSchema(BaseModel):
    parameter_a: constr(min_length=2, max_length=40)  # Constrained Str
    parameter_b: int = Field(..., gt=0, lt=150, description="user age(Human)")

class ResponseSchema(BaseModel):
    status: str

# Clase de ejemplo de un recurso
class Resource:

    @spec.validate(
        json=RequestSchema,
        resp=Response(
            HTTP_200=ResponseSchema,
            HTTP_403=None
        ),
        tags=["api"]
    )
    def on_get(self, request, response):
        """ 
        GET Resources (summary of this endpoint)

        Lorem ipsum dolor sit amet, ... (long description)
        """
        output = {
            "status": "ok"
        }

        response.body = json.dumps(output)
        response.status = falcon.HTTP_200

# Crea una instancia de falcon.App y se configura para que use la instancia de SpecTree:
app = falcon.App()
app.add_route('/resources', Resource())
spec.register(app)


# Lectura de la documentación
# http://localhost:8000/apidoc/swagger
# http://localhost:8000/apidoc/redoc