from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
app=FastAPI()
students= {
        1:{
            "name":"jhon",
            "age": 17,
            "year":"Year 12"
        }
    }

class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year : Optional[str] = None
@app.get("/")
def index():

    return {"name":"Fist Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(None, description="ID of student",gt=0,lt=3)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int,name: str,test : int):
    for student_id in students:
        if students[student_id]["name"]== name:
            return students[student_id]
        return {"Data":"Not found"}




@app.post("/create-student/{student_id}")
def create_student(student_id : int,student : Student):
    if student_id in students:
        return {"Error":"student already exists"}

    students[student_id]=student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Student doesn't exist"}

    if student.name!= None:
        students[student_id].name=student.name
    if student.age!= None:
        students[student_id].age=student.age
    if student.year!= None:
        students[student_id].year=student.year

    return students[student_id]
