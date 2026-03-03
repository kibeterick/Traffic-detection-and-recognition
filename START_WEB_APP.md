# 🌐 Web Interface - Quick Start Guide

## Installation

1. Install Flask (if not already installed):
```bash
pip install flask werkzeug
```

## Starting the Web Server

Run the following command:
```bash
python app.py
```

The server will start on: **http://localhost:5000**

## Using the Web Interface

1. Open your browser and go to: `http://localhost:5000`
2. Click the upload area or drag and drop an image
3. Wait for the prediction (usually takes 1-2 seconds)
4. View the results:
   - Main prediction with confidence score
   - Top 3 predictions
   - Visual feedback

## Features

✨ **Beautiful UI**: Modern, gradient design with smooth animations
📤 **Drag & Drop**: Easy file upload with drag and drop support
🎯 **Instant Results**: Fast predictions with confidence scores
📊 **Top 3 Predictions**: See alternative predictions
📱 **Responsive**: Works on desktop, tablet, and mobile
🔒 **Secure**: File validation and automatic cleanup

## Supported Image Formats

- JPG/JPEG
- PNG
- BMP
- PPM (native GTSRB format)

Maximum file size: 16MB

## API Endpoint

You can also use the API directly:

```bash
curl -X POST -F "file=@path/to/image.jpg" http://localhost:5000/predict
```

Response:
```json
{
  "predicted_class": "Stop",
  "confidence": 99.87,
  "top_3": [
    {"class": "Stop", "confidence": 99.87},
    {"class": "Yield", "confidence": 0.08},
    {"class": "Speed limit (30km/h)", "confidence": 0.03}
  ]
}
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, edit `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
to a different port, e.g., `port=5001`

### Model Not Found
Make sure `traffic_sign_model.h5` is in the same directory as `app.py`

### Import Errors
Install missing dependencies:
```bash
pip install -r requirements.txt
```

## Stopping the Server

Press `CTRL+C` in the terminal where the server is running

## Production Deployment

For production use, consider using:
- **Gunicorn**: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`
- **Nginx**: As a reverse proxy
- **Docker**: For containerized deployment

---

**Enjoy your Traffic Sign Detection Web App! 🚦**
