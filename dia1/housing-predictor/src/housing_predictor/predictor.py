import joblib
import numpy as np
import sklearn
import os

# Obtener ruta del paquete
BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
SCALER_X_PATH = os.path.join(BASE_DIR, "model", "scaler_x.pkl")
SCALER_Y_PATH = os.path.join(BASE_DIR, "model", "scaler_y.pkl")

# cargar modelo solo una vez
model = joblib.load(MODEL_PATH)
sc_x = joblib.load(SCALER_X_PATH)
sc_y = joblib.load(SCALER_Y_PATH)

def predict_price(rooms):
    rooms_sc = sc_x.transform(np.array([[rooms]]))
    prediction_sc = model.predict(rooms_sc)
    prediction = sc_y.inverse_transform(prediction_sc) * 1000
    return float(prediction[0][0])