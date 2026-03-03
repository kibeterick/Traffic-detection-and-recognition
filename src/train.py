import argparse
import os
from data_loader import GTSRBDataLoader
from model import create_model

def train(data_path, epochs=20, batch_size=32):
    print("Loading data...")
    loader = GTSRBDataLoader(data_path)
    X_train, X_test, y_train, y_test = loader.load_data()
    
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    
    print("Creating model...")
    model = create_model()
    model.summary()
    
    print("Training...")
    history = model.fit(
        X_train, y_train,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=(X_test, y_test),
        verbose=1
    )
    
    print("\nEvaluating...")
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test accuracy: {test_acc:.4f}")
    
    model.save('traffic_sign_model.h5')
    print("Model saved as traffic_sign_model.h5")
    
    return history

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default='data/GTSRB', help='Path to GTSRB dataset')
    parser.add_argument('--epochs', type=int, default=20, help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
    
    args = parser.parse_args()
    train(args.data_path, args.epochs, args.batch_size)
