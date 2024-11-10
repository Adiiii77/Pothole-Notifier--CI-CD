from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
model = tf.keras.models.load_model('model/sample.h5')


# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to the input size of the model
    img = image.resize((64, 64))  # Change this size based on your model's expected input
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array


@app.route('/classify', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Load the image file
    image = Image.open(io.BytesIO(file.read()))

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make predictions
    predictions = model.predict(processed_image)
    # Assuming the model outputs probabilities for two classes: pothole (1) and not pothole (0)
    is_pothole = predictions[0][0] > 0.5  # Threshold can be adjusted

    return jsonify({'is_pothole': bool(is_pothole)}), 200

# Add this to each service's app.py
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
