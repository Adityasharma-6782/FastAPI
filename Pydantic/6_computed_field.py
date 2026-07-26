# Field Validator
# ==> It work mainly 2 mode defore and after(default)

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # Kg
    height: float # mtrs
    marriage: bool = False   
    alleragies: Optional[list[str]] = None 
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2))
        return bmi


        

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
    print('BMI:',patient.bmi)

    print("Updated into database")


patient_info = {'name': 'aditya',
                'email': "sharmaadi6782@gmail.com", 
                'age' :'70',
                'weight':80.50,
                'height':1.75,
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