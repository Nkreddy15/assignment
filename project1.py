from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load your model (ensure the model file is named 'your_model.h5' or update the path)
model = tf.keras.models.load_model('your_model.h5')

@app.route('/')
def hello():
    return "Model is live and ready to receive predictions!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON request payload
    data = request.get_json(force=True)
    
    # Assuming input data is a list of numbers, adjust if your input format is different
    input_data = np.array(data['input']).reshape(1, -1)  # Modify based on your model's input shape
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the prediction in JSON format
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
