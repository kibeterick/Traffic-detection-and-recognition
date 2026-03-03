#!/usr/bin/env python3
"""
Simple Dataset Image Viewer
Browse and view traffic sign images from the GTSRB dataset
"""

import os
import cv2
import numpy as np
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

def view_images_by_class(class_id, num_images=5):
    """View sample images from a specific class"""
    class_path = f"data/GTSRB/Final_Training/Images/{class_id:05d}"
    
    if not os.path.exists(class_path):
        print(f"❌ Class {class_id} not found!")
        return
    
    # Get image files
    images = [f for f in os.listdir(class_path) if f.endswith('.ppm')][:num_images]
    
    if not images:
        print(f"❌ No images found in class {class_id}")
        return
    
    print(f"\n{'='*70}")
    print(f"Class {class_id}: {SIGN_NAMES[class_id]}")
    print(f"Total images in class: {len([f for f in os.listdir(class_path) if f.endswith('.ppm')])}")
    print(f"{'='*70}\n")
    
    # Display images
    for i, img_file in enumerate(images, 1):
        img_path = os.path.join(class_path, img_file)
        img = cv2.imread(img_path)
        
        if img is not None:
            # Resize for better viewing
            display_img = cv2.resize(img, (200, 200))
            
            # Add text overlay
            cv2.putText(display_img, f"Class {class_id}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(display_img, f"Image {i}/{len(images)}", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            # Show image
            window_name = f"{SIGN_NAMES[class_id]} - Image {i}"
            cv2.imshow(window_name, display_img)
            
            print(f"✅ Showing: {img_file}")
            print(f"   Size: {img.shape[1]}x{img.shape[0]} pixels")
    
    print(f"\n{'='*70}")
    print("Press any key in the image window to close all images")
    print("Or close the windows manually")
    print(f"{'='*70}\n")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def browse_all_classes():
    """Show one sample image from each class"""
    print("\n" + "="*70)
    print("BROWSING ALL 43 TRAFFIC SIGN CLASSES")
    print("="*70 + "\n")
    
    data_path = "data/GTSRB/Final_Training/Images"
    
    for class_id in range(43):
        class_path = os.path.join(data_path, f'{class_id:05d}')
        
        if not os.path.exists(class_path):
            continue
        
        images = [f for f in os.listdir(class_path) if f.endswith('.ppm')]
        
        if images:
            img_path = os.path.join(class_path, images[0])
            img = cv2.imread(img_path)
            
            if img is not None:
                # Resize for grid display
                display_img = cv2.resize(img, (150, 150))
                
                # Add class label
                cv2.putText(display_img, f"Class {class_id}", (5, 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                # Show image
                cv2.imshow(f"Class {class_id}: {SIGN_NAMES[class_id]}", display_img)
                
                print(f"✅ Class {class_id:2d}: {SIGN_NAMES[class_id]}")
    
    print(f"\n{'='*70}")
    print("All 43 classes displayed!")
    print("Press any key in any image window to close all")
    print(f"{'='*70}\n")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    print("\n" + "="*70)
    print("GTSRB DATASET IMAGE VIEWER")
    print("="*70)
    
    while True:
        print("\nOptions:")
        print("1. View images from a specific class")
        print("2. Browse all 43 classes (one image each)")
        print("3. View popular signs (Stop, Yield, Speed limits)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            try:
                class_id = int(input("Enter class number (0-42): "))
                if 0 <= class_id <= 42:
                    num_images = int(input("How many images to view? (1-10): "))
                    view_images_by_class(class_id, min(num_images, 10))
                else:
                    print("❌ Invalid class number! Must be 0-42")
            except ValueError:
                print("❌ Invalid input! Please enter a number")
        
        elif choice == '2':
            browse_all_classes()
        
        elif choice == '3':
            print("\nViewing popular traffic signs...")
            popular_classes = [0, 1, 2, 13, 14, 17, 25, 33, 38]  # Various popular signs
            for class_id in popular_classes:
                view_images_by_class(class_id, 3)
        
        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-4")

if __name__ == "__main__":
    main()
