import os
import zipfile
import requests
import urllib3
from tqdm import tqdm

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_file(url, destination):
    """Download file with progress bar"""
    response = requests.get(url, stream=True, verify=False)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(destination, 'wb') as file, tqdm(
        desc=destination,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            progress_bar.update(size)

def extract_zip(zip_path, extract_to):
    """Extract zip file"""
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Extraction complete!")

def download_gtsrb_dataset(data_dir='data'):
    """Download GTSRB dataset from Kaggle mirror"""
    os.makedirs(data_dir, exist_ok=True)
    
    # Kaggle dataset URL (public mirror)
    train_url = "https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip"
    
    train_zip = os.path.join(data_dir, "GTSRB_Training.zip")
    
    print("Downloading GTSRB Training Dataset...")
    print("This may take several minutes (around 300MB)...")
    
    try:
        download_file(train_url, train_zip)
        extract_zip(train_zip, data_dir)
        
        # Clean up zip file
        os.remove(train_zip)
        print(f"\nDataset downloaded and extracted to: {data_dir}")
        print("Training images are in: data/GTSRB/Final_Training/Images")
        
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        print("\nAlternative: Download manually from:")
        print("https://benchmark.ini.rub.de/gtsrb_dataset.html")
        print("or https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign")

if __name__ == "__main__":
    download_gtsrb_dataset()
