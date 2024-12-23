from src.cnnClassifier.config.configration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"  # Aşama ismi

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Konfigürasyon yöneticisini oluştur
        config = ConfigurationManager()
        # Veri alım konfigürasyonunu al
        data_ingestion_config = config.get_data_ingestion_config()
        # DataIngestion sınıfını başlat
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # Dosyayı indir
        data_ingestion.download_file()
        # Zip dosyasını çıkar
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat