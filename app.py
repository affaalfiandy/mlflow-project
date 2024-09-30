from flask import Flask, request, jsonify
import pickle
import pandas as pd
from data_preprocessing import impute_age, preprocess  # Adjust the import as needed

# Load the model
with open('models/logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    data = pd.DataFrame([data])
    data["male"] = data['sex']=="male"
    data["Q"] = data["embarked"]=="Q"
    data["S"] = data["embarked"]=="S"
    # Preprocess input data
    input_data = preprocess(data)
    print(input_data)
    # Make prediction
    prediction = model.predict(input_data)
    response = {'survived prediction: ': int(prediction[0])}
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=3000)
