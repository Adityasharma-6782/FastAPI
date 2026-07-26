from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data(): 
    with open('patients.json', 'r') as f: 
        data = json.load(f)
    
    return data


# ====================================== Retrive data ==> get() mathod ======================================================
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

#  =====================================================================================================