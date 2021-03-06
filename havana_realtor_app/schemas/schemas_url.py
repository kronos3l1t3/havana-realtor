from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from havana_realtor_app.schemas.schema.schemaAll import *

urlpatterns = [
    path("",csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
