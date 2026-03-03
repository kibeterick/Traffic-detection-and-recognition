#!/usr/bin/env python3
"""Quick test script to verify model architecture"""

import sys
sys.path.append('src')

from model import create_model
import tensorflow as tf

def test_model():
    print("Testing model architecture...")
    
    # Create model
    model = create_model()
    print("✅ Model created successfully")
    
    # Print model summary
    model.summary()
    
    # Test with dummy data
    import numpy as np
    dummy_input = np.random.random((1, 32, 32, 3))
    prediction = model.predict(dummy_input, verbose=0)
    
    print(f"✅ Model prediction shape: {prediction.shape}")
    print(f"✅ Prediction probabilities sum: {prediction.sum():.4f}")
    print(f"✅ Predicted class: {np.argmax(prediction)}")
    
    print("\n🎉 Model architecture test passed!")

if __name__ == "__main__":
    test_model()