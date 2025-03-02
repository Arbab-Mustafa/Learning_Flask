class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {"username": self.username, "email": self.email}

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):

        return {"name": self.name, "age": self.age, "grade": self.grade}    