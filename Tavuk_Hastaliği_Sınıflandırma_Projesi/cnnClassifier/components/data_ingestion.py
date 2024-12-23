import os
import urllib.request as request
import zipfile
from src.cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config  # Yapılandırma dosyasını yükle

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):  # Dosya yoksa indir
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  # Dosya mevcutsa boyutunu göster

    def extract_zip_file(self):
        """
        zip_file_path: str
        Zip dosyasını veri dizinine açar
        Fonksiyon None döndürür
        """
        unzip_path = self.config.unzip_dir  # Çıkartılacak dizin
        os.makedirs(unzip_path, exist_ok=True)  # Dizin yoksa oluştur
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  # Zip dosyasını aç