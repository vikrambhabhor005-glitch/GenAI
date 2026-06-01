from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

stu=[]

class Students(BaseModel):
    name: str
    enrollment: int
    course: str
        
@app.post("/students/")
def create_student(student: Students):
        stu.append(student.dict())
        return{
            "msg":"Student added successfully",
            "data": stu
        }



@app.get("/GetStudent/")
def get_student():
        return{
            "msg":"Student data recived sucssfully",
            "data":stu
        }

@app.get("/getStudentsbyId/{enrollment}")
def get_student_by_id(enrollment: int):
    for i in stu:
        if i["enrollment"] == enrollment:
            return {
                "msg" : " Student data retrived succesfully",
                "data" : i
            }
    return {
           "msg" : "Student not found"
        } 

@app.put("/updateStudent/{enrollment}")
def update_student(enrollment : int , updated_student : Students):
    for j in stu:
        if j["enrollment"] == enrollment :
            j["name"] = updated_student.name
            j["course"] = updated_student.course
            return {
                 "msg" : "Student data updated sucessfully",
                 "data": j
            }
    return {
        "msg" : "Student not found"
    }

@app.delete("/deletestudent/{enrollment}")
def delete_student(enrollment: int):
    for k in stu:
        if k["enrollment"]== enrollment:
            stu.remove(k)
            return {
                "msg" : "Student data deleted sucessfully",
                "data": k
               }
    return {
         "msg":"Student not found"
        
    }
    
