from flask import Flask,request,render_template
import joblib
import numpy as np
import sklearn

model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    precio = 0
    rooms = 1
    if request.method == "POST":
        rooms = int(request.form['rooms'])
        rooms_sc = sc_x.transform(np.array([[rooms]]))
        prediction_sc = model.predict(rooms_sc)
        prediction = sc_y.inverse_transform(prediction_sc) * 10000
        precio = abs(round(prediction[0][0],2))
    return render_template('index.html',precio=precio,rooms=rooms)

if __name__ == "__main__":
    app.run(debug=True)