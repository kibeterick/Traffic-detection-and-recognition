#!/usr/bin/env python3
"""Quick test to verify setup"""

import os
import sys
sys.path.append('src')

from data_loader import GTSRBDataLoader

def test_data_loading():
    print("Testing data loader...")
    
    # Check if data exists
    data_path = "data/GTSRB"
    if not os.path.exists(data_path):
        print(f"❌ Data path not found: {data_path}")
        return False
    
    # Check Final_Training structure
    images_path = os.path.join(data_path, "Final_Training", "Images")
    if not os.path.exists(images_path):
        print(f"❌ Images path not found: {images_path}")
        return False
    
    # Count classes
    classes = [d for d in os.listdir(images_path) if os.path.isdir(os.path.join(images_path, d))]
    print(f"✅ Found {len(classes)} classes")
    
    # Test loading a small sample
    print("Testing data loader with first 2 classes...")
    loader = GTSRBDataLoader(data_path)
    loader.num_classes = 2  # Test with just 2 classes
    
    try:
        X_train, X_test, y_train, y_test = loader.load_data()
        print(f"✅ Successfully loaded {len(X_train)} training samples")
        print(f"✅ Image shape: {X_train[0].shape}")
        print(f"✅ Labels range: {min(y_train)} to {max(y_train)}")
        return True
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return False

if __name__ == "__main__":
    success = test_data_loading()
    if success:
        print("\n🎉 Setup test passed! Ready for full training.")
    else:
        print("\n❌ Setup test failed. Check the errors above.")