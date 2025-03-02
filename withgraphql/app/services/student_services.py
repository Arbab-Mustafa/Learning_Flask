from app.config.db import db

students_collection = db["students"]


def get_All_students():
     try:
        students = list(students_collection.find({}, {"_id": 0}))
        if not students:
            return None
        return students    
     except Exception as e:
        print(
            f"An error occurred while getting all students. Error: {str(e)}")
        return None


def get_student_by_name(name):
  try:
    student = students_collection.find_one({"name": name}, {"_id": 0})
    if student:
        return student
    return None
  
  except Exception as e:
    print(f"An error occurred while getting student by name. Error: {str(e)}")
    return None
    

def create_student(name, age, grade):
  try:
    student = {"name": name, "age": age, "grade": grade}
    students_collection.insert_one(student)
    return student
     
  except Exception as e:
    print(f"An error occurred while Creating Student Error: {str(e)}")
    return None


def delete_student_name(name):
    try:
        student = students_collection.find_one({"name": name})
        if not student:
            return False  # Student not found
        
        result = students_collection.delete_one({"name": name})
        return result.deleted_count > 0

    except Exception as e:
        print(f"An error occurred while deleting the student. Error: {str(e)}")
        return False


def update_student(name, age, grade):
    try:
        student = {"name": name, "age": age, "grade": grade}
        students_collection.update_one({"name": name}, {"$set": student})
        return student
    except Exception as e:
        print(f"An error occurred while updating student. Error: {str(e)}")
        return None
