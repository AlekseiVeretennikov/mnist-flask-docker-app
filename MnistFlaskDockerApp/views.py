# -*- coding: utf-8 -*- 
from flask import request, jsonify
import joblib
import numpy as np
# Import 'app' from __init__.py in the current folder (MnistFlaskDockerApp package)
from MnistFlaskDockerApp import app  

# Load the model ONCE when the application starts
# The path to the model file is relative to where runserver.py is executed (project root)
model_filename = 'model.joblib' 
model = None # Initialize model as None
try:
    model = joblib.load(model_filename)
    app.logger.info(f"Model '{model_filename}' loaded successfully.") 
except FileNotFoundError:
    app.logger.error(f"Error: Model file '{model_filename}' not found!")
except Exception as e:
    app.logger.error(f"Error loading model: {e}")

# Our single route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if model loaded correctly
    if model is None:
        app.logger.error("Prediction attempt while model is not loaded.")
        return jsonify({"error": "Model not loaded or failed to load"}), 500
        
    # Get data from POST request (expecting JSON)
    data = request.get_json()

    if not data or 'image_data' not in data:
        app.logger.warning("Request to /predict without 'image_data' key.")
        return jsonify({"error": "Key 'image_data' not found in JSON request"}), 400

    # Expect image_data to be a list of 64 numbers (8x8 pixels)
    image_vector = data['image_data']

    if not isinstance(image_vector, list) or len(image_vector) != 64:
        app.logger.warning("Invalid format for 'image_data' in request.")
        return jsonify({"error": "'image_data' must be a list of 64 numbers"}), 400
    
    try:
        # Convert to numpy array and normalize (like in training!)
        # Make sure you divide by the same number (16.0) as during training
        img_array = np.array(image_vector).reshape(1, -1) / 16.0 
        
        # Make prediction
        prediction = model.predict(img_array)
        
        # Return result as JSON
        digit = int(prediction[0]) 
        app.logger.info(f"Prediction for request: {digit}")
        return jsonify({"predicted_digit": digit})

    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({"error": f"Error during prediction: {e}"}), 500
        
# --- Remove any other @app.route definitions from this file ---