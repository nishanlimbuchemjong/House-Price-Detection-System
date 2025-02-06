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

@app.route('/predict', methods=['POST'])
def predict():
    feature_names = [
        'LotArea', 'GrLivArea', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'OverallQual', 'OverallCond',
        'ExterQual', 'BsmtQual', 'KitchenQual', 'YearRemodAdd', 'BedroomAbvGr', 'TotRmsAbvGrd',
        'FullBath', 'HalfBath', 'BsmtFullBath', 'GarageCars', 'GarageArea', 'GarageQual', 'Fireplaces',
        'WoodDeckSF', 'OpenPorchSF', 'PavedDrive'
    ]
    print("Request Form Data:", request.form)  # Debugging line
    data = [float(x) for x in request.form.values()]
    print("Data: ", data)
    final_input = np.array(data).reshape(1, -1)
    print(final_input)
    output = house_price_model.predict(final_input)
    return render_template("home.html", prediction_text="The price prediction is {}".format(output))

# @app.route('/predict', methods=['POST'])
# def predict():
#     feature_names = [
#         'LotArea', 'GrLivArea', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'OverallQual', 'OverallCond',
#         'ExterQual', 'BsmtQual', 'KitchenQual', 'YearRemodAdd', 'BedroomAbvGr', 'TotRmsAbvGrd',
#         'FullBath', 'HalfBath', 'BsmtFullBath', 'GarageCars', 'GarageArea', 'GarageQual', 'Fireplaces',
#         'WoodDeckSF', 'OpenPorchSF', 'PavedDrive'
#     ]
    
#     # Get the form data
#     data = [x for x in request.form.values()]
    
#     # Debugging: Print the received data
#     print("Received form data:", data)
    
#     # Check if the number of features matches
#     if len(data) != len(feature_names):
#         return f"Error: Expected {len(feature_names)} features, but received {len(data)} features.", 400
    
#     # Convert the data to float and reshape it
#     final_input = np.array([float(x) for x in data]).reshape(1, -1)
    
#     # Debugging: Check the shape of the final input
#     print("Final input shape:", final_input.shape)
    
#     # Make prediction
#     output = house_price_model.predict(final_input)
    
#     # Debugging: Print the model output
#     print("Prediction output:", output)
    
#     return render_template("home.html", prediction_text="The price prediction is {}".format(output))

if __name__ == '__main__':
    app.run(debug=True)