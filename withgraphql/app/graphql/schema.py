import graphene
from app.graphql.resolvers import Query

schema = graphene.Schema(query=Query)

