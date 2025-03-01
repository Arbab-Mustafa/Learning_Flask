import graphene 

class UserType(graphene.ObjectType):
    username = graphene.String()
    email = graphene.String()
