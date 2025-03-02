class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):

        return {"name": self.name, "age": self.age, "grade": self.grade} 