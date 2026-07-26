# Data Validation in Pydantic
'''
Pydantic is automaticlt do the type conversion like if you write weight='30.55' then it handle like weight=30.55

 Field:
      ==> Field is use for apply some restrictions on a data type
      ==> Also use for add description in docmentation with the help of Annotated (in typing Module)
      ==> Script is not allow the type conversion in pydantic
 
'''
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    # name: str = Field(max_length=30)  # for normal 
    name: Annotated[str, Field(max_length=30, title="Name of tha patient", description="Enter the name of the Patient in less than 30 words", examples=['Aditya', 'Sharma'])]
    age: int = Field(gt=0, lt=100)
    email: EmailStr   # validate for email
    linkedin_url: AnyUrl     # For check any url
    weight: Annotated[float, Field(gt=0, strict=True)]
    marriage: Annotated[bool, Field(default=False, description="IS the patient married or not?")]
    alleragies: Optional[list[str]] = Field(max_length=5)  #Now it is required
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marriage)
    print(patient.alleragies)
    print(patient.contact_details)
    print("Inserted into database")

def update_patient_data(patient: Patient): 
    # print(patient.name)
    # print(patient.age)
    # print(patient.alleragies)
    # print(patient.marriage)
    print(patient)
    print("Updated into database")


patient_info = {'name': 'aditya', 
                'age' :20,
                'email': 'Adityasharma@gmail.com',
                'linkedin_url': "http://linkedin.com/1234567",
                'weight':80.50,
                'marriage': True,
                'alleragies': ['a','b','c','d','e'],
                'contact_details':{
                    'email': "sharmaadi6782.gmail.com",
                    'phone': '`1234567890'
                    }
                }

patient1= Patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)