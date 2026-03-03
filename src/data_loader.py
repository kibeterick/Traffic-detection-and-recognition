import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tqdm import tqdm

class GTSRBDataLoader:
    def __init__(self, data_path, img_size=(32, 32)):
        self.data_path = data_path
        self.img_size = img_size
        self.num_classes = 43
    
    def load_data(self):
        images = []
        labels = []
        
        # Handle both path formats
        if os.path.exists(os.path.join(self.data_path, 'Final_Training', 'Images')):
            base_path = os.path.join(self.data_path, 'Final_Training', 'Images')
        else:
            base_path = self.data_path
        
        print(f"Loading images from: {base_path}")
        
        # Count total images first for progress bar
        total_images = 0
        for class_id in range(self.num_classes):
            class_path = os.path.join(base_path, f'{class_id:05d}')
            if os.path.exists(class_path):
                total_images += len([f for f in os.listdir(class_path) if f.endswith(('.ppm', '.jpg', '.png'))])
        
        print(f"Found {total_images} images across {self.num_classes} classes")
        
        with tqdm(total=total_images, desc="Loading images") as pbar:
            for class_id in range(self.num_classes):
                class_path = os.path.join(base_path, f'{class_id:05d}')
                if not os.path.exists(class_path):
                    continue
                    
                for img_file in os.listdir(class_path):
                    if img_file.endswith(('.ppm', '.jpg', '.png')):
                        img_path = os.path.join(class_path, img_file)
                        img = cv2.imread(img_path)
                        if img is not None:
                            img = cv2.resize(img, self.img_size)
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            images.append(img)
                            labels.append(class_id)
                        pbar.update(1)
        
        print(f"Loaded {len(images)} images successfully")
        images = np.array(images, dtype='float32') / 255.0
        labels = np.array(labels)
        
        return train_test_split(images, labels, test_size=0.2, random_state=42)
