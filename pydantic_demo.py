from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name : str = 'karan' #setting a default value incase name is empty
    age: Optional[int] = None #similar optional in typedDict
    email: EmailStr #only to validate emails
    cgpa: float=Field(gt=0,lt=10,default=6.9,description='a value representing how gdha student is') #for cgpa to be >0 and <10 always
    interest: str = Field(description="Interest of student/hobby")
    
new_student = {'name':'rajshree', 'email':'xyz@yahoo.com','cgpa':9.4}

student = Student(**new_student)

print(student)
#for pydantic obj
print(student.name)
#for dict
print(student['name'])

#pydantic->dict conversion
print(dict(student))
#pydantic->json
student_json = student.model_dump_json()

