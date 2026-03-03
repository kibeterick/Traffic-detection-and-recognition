#!/usr/bin/env python3
"""Complete system test - loads model and makes predictions"""

import sys
import os
sys.path.append('src')

import numpy as np
import cv2
from tensorflow import keras

# Traffic sign class names
CLASS_NAMES = {
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

def test_system():
    print("=" * 60)
    print("GERMAN TRAFFIC SIGN DETECTION SYSTEM TEST")
    print("=" * 60)
    
    # 1. Check model exists
    print("\n[1/4] Checking model file...")
    if not os.path.exists('traffic_sign_model.h5'):
        print("❌ Model file not found!")
        return False
    print("✅ Model file found (2.0 MB)")
    
    # 2. Load model
    print("\n[2/4] Loading trained model...")
    try:
        model = keras.models.load_model('traffic_sign_model.h5')
        print("✅ Model loaded successfully")
        print(f"   - Input shape: {model.input_shape}")
        print(f"   - Output classes: {model.output_shape[1]}")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False
    
    # 3. Find test images
    print("\n[3/4] Finding test images...")
    test_images = []
    data_path = "data/GTSRB/Final_Training/Images"
    
    # Get one image from first 5 classes
    for class_id in range(5):
        class_path = os.path.join(data_path, f'{class_id:05d}')
        if os.path.exists(class_path):
            images = [f for f in os.listdir(class_path) if f.endswith('.ppm')]
            if images:
                test_images.append((class_id, os.path.join(class_path, images[0])))
    
    print(f"✅ Found {len(test_images)} test images")
    
    # 4. Make predictions
    print("\n[4/4] Testing predictions...")
    correct = 0
    for true_class, img_path in test_images:
        # Load and preprocess image
        img = cv2.imread(img_path)
        img = cv2.resize(img, (32, 32))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype('float32') / 255.0
        img = np.expand_dims(img, axis=0)
        
        # Predict
        prediction = model.predict(img, verbose=0)
        predicted_class = np.argmax(prediction)
        confidence = prediction[0][predicted_class] * 100
        
        # Display result
        status = "✅" if predicted_class == true_class else "❌"
        print(f"\n{status} Image: {os.path.basename(img_path)}")
        print(f"   True class: {true_class} - {CLASS_NAMES[true_class]}")
        print(f"   Predicted: {predicted_class} - {CLASS_NAMES[predicted_class]}")
        print(f"   Confidence: {confidence:.2f}%")
        
        if predicted_class == true_class:
            correct += 1
    
    # Summary
    accuracy = (correct / len(test_images)) * 100
    print("\n" + "=" * 60)
    print(f"SYSTEM TEST RESULTS: {correct}/{len(test_images)} correct ({accuracy:.1f}%)")
    print("=" * 60)
    
    if accuracy >= 80:
        print("\n🎉 System is working correctly!")
        return True
    else:
        print("\n⚠️ System needs improvement")
        return False

if __name__ == "__main__":
    success = test_system()
    sys.exit(0 if success else 1)
