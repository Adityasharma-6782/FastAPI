# Field Validator
# ==> It work mainly 2 mode defore and after(default)

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    marriage: bool = False   
    alleragies: Optional[list[str]] = None 
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valide_domains = ['sbi.com','hdfc.com','icici.com']

        domain_value = value.split('@')[-1]

        if domain_value not in valide_domains:
            raise TypeError("Domain is not valide")
        
        return value


    @field_validator('name')
    @classmethod
    def name_transforms(cls, value): 
        return value.upper()


    # @field_validator('age', mode='before') # It gives error due to age in str before type conversion
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else: 
            raise TypeError("Age should be b/w from 0 to 100")

        

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
                'age' :'20',
                'weight':80.50,
                'marriage': True,
                # 'alleragies': ['pollen', 'dust'],
                'contact_details':{
                    'phone': '`1234567890'
                    }
                }

patient1= Patient(**patient_info)
# insert_patient_data(patient1)
update_patient_data(patient1)