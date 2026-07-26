from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the patient", examples=["P001"])] 
    name: Annotated[str, Field(..., description="Name od the patient")]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age od the Patient")]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in mtrs")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in kg")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2),2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi < 30 :
            return 'Overweight'
        else:
            return 'Obese'

def load_data(): 
    with open('patients.json', 'r') as f: 
        data = json.load(f)
    
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


@app.get("/")
def hello(): 
    return {'message': "Patients Managment System API"}

@app.get("/about")
def hello(): 
    return {'message': "Fully functional API to manage your patients"}


@app.get('/view')
def view():
    data = load_data()
    return data

# @app.get('/patient/{patient_id}')
# def view_patient(patient_id: str): 
#     data = load_data()

#     if patient_id in data: 
#         return data[patient_id]
#     else: 
#         return {"Message":"Not Found"}



# After import path parameters----------------------
# @app.get('/patient/{patient_id}')
# def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')): 
#     data = load_data()

#     if patient_id in data: 
#         return data[patient_id]
#     else: 
#         return {"Message":"Not Found"}
    


# After HTTPException-----------------------
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')): 
    data = load_data()

    if patient_id in data: 
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient Not Found")   # When patient not found show 404



# Query Parameter
@app.get('/sort')
def sort_patient(sort_by: str = Query(..., description="sort on the basis of height, weight or bmi"), order: str = Query('asc', description="Sort in asc or casc order")):

    valid_flides = ['height', 'weight', 'bmi', 'age']

    if sort_by not in valid_flides:
        raise HTTPException(status_code=404, detail=f'Invalide field select from {valid_flides}')

    if order not in ['asc', 'dasc']:
        raise HTTPException(status_code=404, detail='Invalide order select b/w asc or dasc')
    
    data = load_data()
    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):

    # load existing data
    data = load_data() 

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message': "Patient created successfully"})
    