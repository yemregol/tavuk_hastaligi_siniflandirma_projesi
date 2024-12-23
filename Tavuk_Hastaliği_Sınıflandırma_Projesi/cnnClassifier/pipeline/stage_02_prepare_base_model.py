from src.cnnClassifier.config.configration import ConfigurationManager
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.cnnClassifier import logger

STAGE_NAME = "Prepare base model"  # Aşama ismi

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Konfigürasyon yöneticisini oluştur
        config = ConfigurationManager()
        # Temel model konfigürasyonunu al
        prepare_base_model_config = config.get_prepare_base_model_config()
        # PrepareBaseModel sınıfını başlat
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        # Temel modeli al
        prepare_base_model.get_base_model()
        # Temel modeli güncelle
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat