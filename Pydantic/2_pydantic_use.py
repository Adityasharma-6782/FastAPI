from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    marriage: bool = False    # It is not an optional by default value is False
    alleragies: Optional[list[str]] = None   # It is optional
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
                'weight':80.50,
                'marriage': True,
                # 'alleragies': ['pollen', 'dust'],
                'contact_details':{
                    'email': "sharmaadi6782.gmail.com",
                    'phone': '`1234567890'
                    }
                }

patient1= Patient(**patient_info)
insert_patient_data(patient1)
update_patient_data(patient1)