import json
import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import os  # 👈 for environment variables

app = Flask(__name__)

# Load the model and scaler safely using context manager
with open('house.pkl', 'rb') as model_file:
    regmodel = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scalar = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    arr = np.array(list(data.values())).reshape(1, -1)
    print(arr)
    new_data = scalar.transform(arr)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template(
        "home.html",
        prediction_text=f"The House price prediction is {output}"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # ✅ Railway sets PORT env variable
    app.run(host="0.0.0.0", port=port)
