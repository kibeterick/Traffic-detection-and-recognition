# 🚦 Traffic Detection and Recognition System

A deep learning-based web application for detecting and classifying German traffic signs using Convolutional Neural Networks (CNN).

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-orange.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-97.62%25-success.svg)

## 🎯 Features

- **High Accuracy**: 97.62% validation accuracy on GTSRB dataset
- **43 Traffic Sign Classes**: Detects all German traffic sign categories
- **Web Interface**: Beautiful, user-friendly drag-and-drop interface
- **Real-time Predictions**: Get instant results with confidence scores
- **Sample Gallery**: Built-in gallery with test images
- **Easy to Use**: Simple setup and deployment

## 📊 Model Performance

- **Training Accuracy**: 91.42%
- **Validation Accuracy**: 97.62%
- **Dataset**: GTSRB (German Traffic Sign Recognition Benchmark)
- **Training Images**: 39,209 images
- **Classes**: 43 different traffic signs

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/traffic-sign-detection.git
cd traffic-sign-detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the dataset:
```bash
python src/download_dataset.py
```

4. Train the model (optional - pre-trained model included):
```bash
python src/train.py --data_path data/GTSRB --epochs 10
```

5. Start the web application:
```bash
python app.py
```

6. Open your browser and go to: `http://localhost:5000`

## 🖥️ Usage

### Web Interface

1. Start the server: `python app.py`
2. Open browser: `http://localhost:5000`
3. Upload an image or click a sample image
4. Get instant prediction with confidence score

### Command Line

```bash
python src/predict.py --image_path path/to/image.jpg
```

### Python API

```python
from tensorflow import keras
import cv2
import numpy as np

# Load model
model = keras.models.load_model('traffic_sign_model.h5')

# Preprocess image
img = cv2.imread('image.jpg')
img = cv2.resize(img, (32, 32))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.astype('float32') / 255.0
img = np.expand_dims(img, axis=0)

# Predict
prediction = model.predict(img)
class_id = np.argmax(prediction[0])
confidence = prediction[0][class_id]
```

## 📁 Project Structure

```
traffic-sign-detection/
├── app.py                      # Flask web application
├── requirements.txt            # Python dependencies
├── traffic_sign_model.h5       # Trained model (download separately)
│
├── src/
│   ├── train.py               # Training script
│   ├── predict.py             # Prediction script
│   ├── model.py               # CNN model architecture
│   ├── data_loader.py         # Data loading utilities
│   └── download_dataset.py    # Dataset downloader
│
├── templates/
│   └── index.html             # Web interface
│
└── docs/
    ├── HOW_TO_USE.md          # Detailed usage guide
    └── FINAL_SUMMARY.md       # Complete documentation
```

## 🎨 Traffic Sign Classes

The system can detect 43 different German traffic signs:

| Class | Sign Name | Class | Sign Name |
|-------|-----------|-------|-----------|
| 0 | Speed limit (20km/h) | 22 | Bumpy road |
| 1 | Speed limit (30km/h) | 23 | Slippery road |
| 2 | Speed limit (50km/h) | 24 | Road narrows on the right |
| 3 | Speed limit (60km/h) | 25 | Road work |
| 4 | Speed limit (70km/h) | 26 | Traffic signals |
| 5 | Speed limit (80km/h) | 27 | Pedestrians |
| 6 | End of speed limit (80km/h) | 28 | Children crossing |
| 7 | Speed limit (100km/h) | 29 | Bicycles crossing |
| 8 | Speed limit (120km/h) | 30 | Beware of ice/snow |
| 9 | No passing | 31 | Wild animals crossing |
| 10 | No passing (3.5t+) | 32 | End of limits |
| 11 | Right-of-way | 33 | Turn right ahead |
| 12 | Priority road | 34 | Turn left ahead |
| 13 | Yield | 35 | Ahead only |
| 14 | Stop | 36 | Go straight or right |
| 15 | No vehicles | 37 | Go straight or left |
| 16 | Vehicles (3.5t+) prohibited | 38 | Keep right |
| 17 | No entry | 39 | Keep left |
| 18 | General caution | 40 | Roundabout mandatory |
| 19 | Dangerous curve left | 41 | End of no passing |
| 20 | Dangerous curve right | 42 | End of no passing (3.5t+) |
| 21 | Double curve | | |

## 🧠 Model Architecture

- **Type**: Convolutional Neural Network (CNN)
- **Input**: 32x32x3 RGB images
- **Layers**:
  - 3 Convolutional layers with MaxPooling
  - Dropout for regularization
  - Dense layers for classification
- **Output**: 43 classes (softmax activation)
- **Optimizer**: Adam
- **Loss**: Sparse Categorical Crossentropy

## 📦 Dependencies

- TensorFlow >= 2.13.0
- Flask >= 2.0.0
- OpenCV >= 4.8.0
- NumPy >= 1.24.0
- Pillow >= 10.0.0
- scikit-learn >= 1.3.0

## 🔧 Configuration

### Training Parameters

Edit `src/train.py` to adjust:
- `epochs`: Number of training epochs (default: 20)
- `batch_size`: Batch size for training (default: 32)
- `img_size`: Input image size (default: 32x32)

### Web Server

Edit `app.py` to change:
- `host`: Server host (default: 127.0.0.1)
- `port`: Server port (default: 5000)
- `debug`: Debug mode (default: False)

## 📝 Dataset

This project uses the **GTSRB (German Traffic Sign Recognition Benchmark)** dataset:
- **Source**: [GTSRB Official](https://benchmark.ini.rub.de/)
- **Images**: 39,209 training images
- **Classes**: 43 traffic sign categories
- **Format**: PPM images (various sizes)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- GTSRB dataset creators
- TensorFlow and Keras teams
- Flask framework
- OpenCV community

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Made with ❤️ for traffic safety and AI education**
