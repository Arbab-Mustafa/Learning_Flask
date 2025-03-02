import graphene 

class UserType(graphene.ObjectType):
    username = graphene.String()
    email = graphene.String()

class StudentType(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()
    grade = graphene.String()

    