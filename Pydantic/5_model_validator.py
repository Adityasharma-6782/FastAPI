# Field Validator
# ==> It work mainly 2 mode defore and after(default)

from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    marriage: bool = False   
    alleragies: Optional[list[str]] = None 
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age >= 60 and 'emergency' not in model.contact_details:
            raise TypeError("Patient older then 60 must have an emergency contact")
        return model


        

def insert_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.marriage)
    print(patient.alleragies)
    print(patient.contact_details)
    print("Inserted into database")

def update_patient_data(patient: Patient): 
    print(patient)
    print("Updated into database")


patient_info = {'name': 'aditya',
                'email': "sharmaadi6782@sbi.com", 
                'age' :'70',
                'weight':80.50,
                'marriage': True,
                # 'alleragies': ['pollen', 'dust'],
                'contact_details':{
                    'phone': '`1234567890',
                    'emergency': '12346'
                    }
                }

patient1= Patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)