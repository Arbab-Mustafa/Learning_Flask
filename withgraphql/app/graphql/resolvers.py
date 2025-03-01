from graphene import ObjectType, Field, String, Mutation
from app.services.user_service import get_user_by_username, create_user, delete_user , get_all_users 
from app.graphql.types import UserType
import graphene

class Query(ObjectType):
    get_user = Field(UserType, username=String(required=True))
    get_all_users = graphene.List(UserType)

    def resolve_get_user(root, info, username):
        user = get_user_by_username(username)
        if user:
            return UserType(username=user["username"], email=user["email"])
        return None

    def resolve_get_all_users(root, info):
        users = get_all_users()
        return [UserType(username=user["username"], email=user["email"]) for user in users]  # ✅ Fix mapping



class CreateUser(Mutation):
    class Arguments:
        username = String(required=True)
        email = String(required=True)

    user = Field(UserType)

    def mutate(root, info, username, email):
        user_data = create_user(username, email)
        return CreateUser(user=UserType(username=user_data["username"], email=user_data["email"]))

class DeleteUser(Mutation):
    class Arguments:
        username = String(required=True)

    success = String()

    def mutate(root, info, username):
        if delete_user(username):
            return DeleteUser(success="User deleted successfully")
        return DeleteUser(success="User not found")

class Mutation(ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()



