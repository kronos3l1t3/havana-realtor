from havana_realtor_app.authentication.schemas.schemaBasicLogin import *
from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, Auth, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
