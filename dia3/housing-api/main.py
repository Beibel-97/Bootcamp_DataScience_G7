import joblib
import numpy as np
import sklearn
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = FastAPI()

#schema
class Housing(BaseModel):
    rooms: int

@app.get("/")
def home():
    return {"message": "Housing API"}

@app.post("/housing_price")
def housing_price(housing: Housing):
    rooms = housing.rooms
    rooms_sc = sc_x.transform(np.array([[rooms]]))
    prediction_sc = model.predict(rooms_sc)
    prediction = sc_y.inverse_transform(prediction_sc) * 1000
    price = round(prediction[0][0],2)
    
    return {
        "rooms":rooms,
        "price":price
    }