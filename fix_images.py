#!/usr/bin/env python3
"""
Fix image conversion - properly convert PPM to JPG with correct color handling
"""

import os
import cv2
import numpy as np
from PIL import Image

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

def convert_with_pil(ppm_path, jpg_path):
    """Convert PPM to JPG using PIL (better compatibility)"""
    try:
        img = Image.open(ppm_path)
        img = img.convert('RGB')  # Ensure RGB mode
        img.save(jpg_path, 'JPEG', quality=95)
        return True
    except Exception as e:
        print(f"   ❌ PIL failed: {e}")
        return False

def convert_with_opencv(ppm_path, jpg_path):
    """Convert PPM to JPG using OpenCV"""
    try:
        img = cv2.imread(ppm_path)
        if img is None:
            return False
        # Convert BGR to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Convert back to BGR for saving
        cv2.imwrite(jpg_path, img)
        return True
    except Exception as e:
        print(f"   ❌ OpenCV failed: {e}")
        return False

def fix_images():
    """Re-convert images with better handling"""
    
    # Create output folder
    output_folder = "sample_images_fixed"
    os.makedirs(output_folder, exist_ok=True)
    
    print("\n" + "="*70)
    print("FIXING IMAGE CONVERSION - USING PIL FOR BETTER COMPATIBILITY")
    print("="*70 + "\n")
    
    data_path = "data/GTSRB/Final_Training/Images"
    total_converted = 0
    failed = 0
    
    # Convert 5 images from each class
    for class_id in range(43):
        class_path = os.path.join(data_path, f'{class_id:05d}')
        
        if not os.path.exists(class_path):
            continue
        
        # Get first 5 images
        images = [f for f in os.listdir(class_path) if f.endswith('.ppm')][:5]
        
        for i, img_file in enumerate(images, 1):
            ppm_path = os.path.join(class_path, img_file)
            
            # Create descriptive filename
            sign_name = SIGN_NAMES[class_id].replace('/', '-').replace(' ', '_').replace('(', '').replace(')', '')
            output_name = f"class_{class_id:02d}_{sign_name}_sample{i}.jpg"
            jpg_path = os.path.join(output_folder, output_name)
            
            # Try PIL first (better for PPM), then OpenCV
            if convert_with_pil(ppm_path, jpg_path):
                total_converted += 1
                if i == 1:  # Print once per class
                    print(f"✅ Class {class_id:2d}: {SIGN_NAMES[class_id]}")
            elif convert_with_opencv(ppm_path, jpg_path):
                total_converted += 1
                if i == 1:
                    print(f"✅ Class {class_id:2d}: {SIGN_NAMES[class_id]} (OpenCV)")
            else:
                failed += 1
                if i == 1:
                    print(f"❌ Class {class_id:2d}: Failed to convert")
    
    print(f"\n{'='*70}")
    print(f"✅ Successfully converted: {total_converted} images")
    if failed > 0:
        print(f"❌ Failed: {failed} images")
    print(f"📁 Location: {os.path.abspath(output_folder)}")
    print(f"{'='*70}\n")
    print("Try opening images from 'sample_images_fixed' folder now!")
    print("These should display correctly in any image viewer.\n")

if __name__ == "__main__":
    fix_images()
