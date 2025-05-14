from pydantic import BaseModel
from typing import List

# TODO: Create Course model
# Each Course has Modules
# Each Modules has  lessons

class Lesson(BaseModel):
    lesson_id: int
    tropic: str

class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]

class Course(BaseModel):
    course_id: int
    course_name: str
    student_name: str
    modules: List[Module]