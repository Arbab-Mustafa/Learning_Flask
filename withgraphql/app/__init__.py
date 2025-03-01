from flask import Flask
from flask_graphql import GraphQLView
from app.graphql.resolvers import Query, Mutation
import graphene

app = Flask(__name__)

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
)
