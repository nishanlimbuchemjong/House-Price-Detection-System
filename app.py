from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# load the model:
house_price_model = pickle.load(open('modified_house_price_model.pkl', 'rb'))
scaler = pickle.load(open('modified_scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     data = request.json
#     # print(np.array(list(data.values())).reshape(1,-1))
#     # new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
#     output = house_price_model.predict(data)
#     print(output[0])
#     return jsonify(output[0])

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Get the JSON data from the request
    data = request.json

    # Extract the feature values from the data (make sure this order matches the features used to train the model)
    feature_names = [
        'LotArea', 'GrLivArea', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'OverallQual', 'OverallCond',
        'ExterQual', 'BsmtQual', 'KitchenQual', 'YearRemodAdd', 'BedroomAbvGr', 'TotRmsAbvGrd',
        'FullBath', 'HalfBath', 'BsmtFullBath', 'GarageCars', 'GarageArea', 'GarageQual', 'Fireplaces',
        'WoodDeckSF', 'OpenPorchSF', 'PavedDrive'
    ]
    
    # Extract the values and ensure the data is in the correct shape for the model
    input_features = np.array([data[feature] for feature in feature_names]).reshape(1, -1)
    
    # Apply the scaling transformation
    # scaled_input = scaler.transform(input_features)
    
    # Make the prediction
    predicted_price = house_price_model.predict(input_features)
    
    # Return the predicted price as a JSON response
    return jsonify(predicted_price[0])

if __name__ == '__main__':
    app.run(debug=True)