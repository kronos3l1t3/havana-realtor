from havana_realtor_app.authentication.schemas.schemaBasicLogin import *
from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery, MeQuery, graphene.ObjectType):
    """
        General Query Classes, this is the place to put all the classes in the software to generate endpoints and to make query's in the database
    """
    pass

class Mutation(AuthMutation, Auth, graphene.ObjectType):
    """
        General Mutations Classes, this is the place to put all the classes in the software to generate endpoints and to make mutation in the database
    """
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
