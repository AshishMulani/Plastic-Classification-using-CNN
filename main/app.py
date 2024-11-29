from flask import Flask, request, jsonify, render_template
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Path to the trained model
MODEL_PATH = r"D:\Shubham\study\Project\Plastic Classification\New folder\resnet50.h5"

# Load the model
model = load_model(MODEL_PATH)

# Define the allowed extensions for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define routes
@app.route('/')
def index():
    return render_template('index.html')  # Ensure the HTML code provided is saved as `templates/index.html`

@app.route('/classify', methods=['POST'])
def classify_plastic():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for upload'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)

        # Save the file to the server
        file.save(filepath)

        # Preprocess the image
        image = load_img(filepath, target_size=(224, 224))  # Adjust size based on model requirements
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0) / 255.0  # Normalize pixel values

        # Predict using the model
        predictions = model.predict(image)
        class_index = np.argmax(predictions, axis=1)[0]

        # Define plastic type classes
        classes = [
            "HDPE (High-Density Polyethylene)",
            "LDPE (Low-Density Polyethylene)",
            "PET (Polyethylene Terephthalate)",
            "PP (Polypropylene)",
            "PS (Polystyrene)",
            "PVC (Polyvinyl Chloride)"
        ]

        # Get the corresponding class label
        result = classes[class_index]

        # Return the result as JSON
        return jsonify({'classification': result})

    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    # Create uploads folder if it doesn't exist
    os.makedirs('uploads', exist_ok=True)

    # Run the Flask app
    app.run(debug=True)
