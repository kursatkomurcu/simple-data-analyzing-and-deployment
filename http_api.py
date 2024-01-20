import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('top_model.sav')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    df = pd.DataFrame([data])
    x_test = np.array(df)
    
    pred = model.predict(x_test)

    return jsonify({'predicted_gdp_per_capita' : pred[0]})

if __name__ == '__main__':
    app.run(debug=True)
