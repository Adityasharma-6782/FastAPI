from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema. input import user_input
from Model.predict import predict_output,model, MODEl_VERSION
from schema.prediction_response import PredictionResponse


app = FastAPI()


# human reagable
@app.get('/')
def home():
    return {'message': 'This is home page and go to the docs'}

# machine reagable
@app.get('/health')
def health_check():
    return {
        'status': 'Ok',
        'version': MODEl_VERSION,
        'model_loaded': model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
def predict_primium(data: user_input):
    input_df ={
        'bmi': data.bmi,
        "age_group": data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(input_df)
        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))