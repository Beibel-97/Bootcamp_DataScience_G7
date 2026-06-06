import joblib
import numpy as np
import sklearn

model =  joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

print("modelos cargados...")

rooms = int(input("Ingrese el nro de habitaciones :"))
rooms_np = np.array([[rooms]])
rooms_sc = sc_x.transform(rooms_np)

print(f"ROOMS ESCALADO :{rooms_sc}")
prediction_sc = model.predict(rooms_sc)
print(f"PREDICTION SC : {prediction_sc}")
prediction = sc_y.inverse_transform(prediction_sc)
print(f'El precio de una casa con {rooms} habitaciones es : $ {prediction[0][0]:.2f} M')