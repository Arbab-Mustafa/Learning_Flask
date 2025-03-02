from graphene import ObjectType, Field, String, Mutation , Int
from app.services.user_service import get_user_by_username, create_user, delete_user , get_all_users  
from app.graphql.types import UserType , StudentType 
import graphene

# --add student ---
from app.services.student_services import get_All_students , get_student_by_name , create_student


class Query(ObjectType):
    get_user = Field(UserType, username=String(required=True)) 
    get_all_users = graphene.List(UserType)
    # --add student ---
    get_all_students = graphene.List(StudentType)
    get_student_by_name = Field(StudentType, name=String(required=True))


    def resolve_get_all_students(root, info):
        students = get_All_students()
        return [StudentType(name=student["name"], age=student["age"], grade=student["grade"]) for student in students]

    
    def resolve_get_student_by_name(root, info, name):
        student = get_student_by_name(name)
        if student:
            return StudentType(name=student["name"], age=student["age"], grade=student["grade"])

        return None    



# ----------
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


class CreateStudent(Mutation):
    class Arguments:
        name = String(required=True)
        age = Int(required=True)
        grade = String(required=True)

    
    student = Field(StudentType)

    def mutate(root, info, name, age, grade):       
        student =  create_student(name, age, grade)
        return CreateStudent(student=StudentType(name=student["name"], age=student["age"], grade=student["grade"]))



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
    create_student = CreateStudent.Field()








