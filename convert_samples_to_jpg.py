#!/usr/bin/env python3
"""
Convert sample PPM images to JPG format for easy viewing
Creates a 'sample_images' folder with JPG versions
"""

import os
import cv2
from pathlib import Path

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

def convert_samples():
    """Convert sample images from each class to JPG"""
    
    # Create output folder
    output_folder = "sample_images"
    os.makedirs(output_folder, exist_ok=True)
    
    print("\n" + "="*70)
    print("CONVERTING SAMPLE IMAGES TO JPG FORMAT")
    print("="*70 + "\n")
    
    data_path = "data/GTSRB/Final_Training/Images"
    total_converted = 0
    
    # Convert 3 images from each class
    for class_id in range(43):
        class_path = os.path.join(data_path, f'{class_id:05d}')
        
        if not os.path.exists(class_path):
            continue
        
        # Get first 3 images
        images = [f for f in os.listdir(class_path) if f.endswith('.ppm')][:3]
        
        for i, img_file in enumerate(images, 1):
            img_path = os.path.join(class_path, img_file)
            img = cv2.imread(img_path)
            
            if img is not None:
                # Create descriptive filename
                sign_name = SIGN_NAMES[class_id].replace('/', '-').replace(' ', '_')
                output_name = f"class_{class_id:02d}_{sign_name}_sample{i}.jpg"
                output_path = os.path.join(output_folder, output_name)
                
                # Save as JPG
                cv2.imwrite(output_path, img)
                total_converted += 1
                
                if i == 1:  # Print once per class
                    print(f"✅ Class {class_id:2d}: {SIGN_NAMES[class_id]}")
    
    print(f"\n{'='*70}")
    print(f"✅ Converted {total_converted} images to JPG format")
    print(f"📁 Location: {os.path.abspath(output_folder)}")
    print(f"{'='*70}\n")
    print("You can now open these JPG files with any image viewer!")
    print("Double-click any image in the 'sample_images' folder to view it.\n")

if __name__ == "__main__":
    convert_samples()
