from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello(): 
    return {'message': "Hello Boy's"}

@app.get("/me")
def hello(): 
    return {'message': "I'm Aditya Kuamr Sharma and i'm developed an eye infection"}