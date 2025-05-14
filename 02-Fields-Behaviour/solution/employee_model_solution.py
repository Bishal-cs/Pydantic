from pydantic import BaseModel, Field
from typing import Optional

# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General' )
# - salary: float (must be >= 10000)

class Employee(BaseModel):
    id : int
    name : str = Field(
        # This is all From Field from Pydentic
        ..., # This means This is the required 
        min_length = 3, 
        max_length = 50,
        description = "Employee Name",
        examples = "Bishal Das"
    )
    department : Optional[str] = "General"
    salary : float = Field(
        ...,
        ge = 10000
    )