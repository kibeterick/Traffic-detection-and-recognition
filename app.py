#!/usr/bin/env python3
"""
Flask Web Application for German Traffic Sign Detection
Upload an image and get instant predictions
"""

from flask import Flask, render_template, request, jsonify
import os
import cv2
import numpy as np
from tensorflow import keras
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'ppm', 'bmp'}

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Traffic sign class names
SIGN_NAMES = {
    0: 'Speed limit (20km/h)', 1: 'Speed limit (30km/h)', 2: 'Speed limit (50km/h)',
    3: 'Speed limit (60km/h)', 4: 'Speed limit (70km/h)', 5: 'Speed limit (80km/h)',
    6: 'End of speed limit (80km/h)', 7: 'Speed limit (100km/h)', 8: 'Speed limit (120km/h)',
    9: 'No passing', 10: 'No passing for vehicles over 3.5 metric tons',
    11: 'Right-of-way at the next intersection', 12: 'Priority road', 13: 'Yield',
    14: 'Stop', 15: 'No vehicles', 16: 'Vehicles over 3.5 metric tons prohibited',
    17: 'No entry', 18: 'General caution', 19: 'Dangerous curve to the left',
    20: 'Dangerous curve to the right', 21: 'Double curve', 22: 'Bumpy road',
    23: 'Slippery road', 24: 'Road narrows on the right', 25: 'Road work',
    26: 'Traffic signals', 27: 'Pedestrians', 28: 'Children crossing',
    29: 'Bicycles crossing', 30: 'Beware of ice/snow', 31: 'Wild animals crossing',
    32: 'End of all speed and passing limits', 33: 'Turn right ahead',
    34: 'Turn left ahead', 35: 'Ahead only', 36: 'Go straight or right',
    37: 'Go straight or left', 38: 'Keep right', 39: 'Keep left',
    40: 'Roundabout mandatory', 41: 'End of no passing',
    42: 'End of no passing by vehicles over 3.5 metric tons'
}

# Load model at startup
print("Loading model...")
model = keras.models.load_model('traffic_sign_model.h5')
print("Model loaded successfully!")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def predict_image(image_path):
    """Predict traffic sign from image"""
    # Load and preprocess image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (32, 32))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    
    # Make prediction
    predictions = model.predict(img, verbose=0)
    class_id = np.argmax(predictions[0])
    confidence = float(predictions[0][class_id])
    
    # Get top 3 predictions
    top_3_indices = np.argsort(predictions[0])[-3:][::-1]
    top_3_predictions = [
        {
            'class': SIGN_NAMES[idx],
            'confidence': float(predictions[0][idx] * 100)
        }
        for idx in top_3_indices
    ]
    
    return {
        'predicted_class': SIGN_NAMES[class_id],
        'confidence': confidence * 100,
        'top_3': top_3_predictions
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sample_images')
def get_sample_images():
    """Get list of sample images"""
    sample_folder = 'sample_images_fixed'
    if not os.path.exists(sample_folder):
        return jsonify({'images': []})
    
    images = []
    for filename in sorted(os.listdir(sample_folder))[:30]:  # First 30 images
        if filename.endswith('.jpg'):
            images.append({
                'filename': filename,
                'path': f'/static/samples/{filename}'
            })
    
    return jsonify({'images': images})

@app.route('/static/samples/<filename>')
def serve_sample(filename):
    """Serve sample images"""
    from flask import send_from_directory
    return send_from_directory('sample_images_fixed', filename)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            result = predict_image(filepath)
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Clean up uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'model_loaded': True})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Traffic Detection and Recognition System")
    print("="*60)
    print("\nStarting server...")
    print("Open your browser and go to: http://localhost:5000")
    print("\nPress CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)
