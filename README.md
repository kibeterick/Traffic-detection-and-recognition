# German Traffic Sign Detection

Bildverarbeitungsprojekt zur Erkennung deutscher Verkehrszeichen mit dem GTSRB-Benchmark.

## Installation

```bash
pip install -r requirements.txt
```

## Dataset

Download GTSRB dataset from: https://benchmark.ini.rub.de/gtsrb_dataset.html
Extract to `data/` directory.

## Usage

### Training
```bash
python src/train.py --data_path data/GTSRB --epochs 20
```

### Prediction
```bash
python src/predict.py --image_path path/to/sign.jpg --model_path model.h5
```

## Model

CNN architecture with:
- 3 Convolutional layers
- MaxPooling
- Dropout for regularization
- 43 classes (GTSRB categories)
