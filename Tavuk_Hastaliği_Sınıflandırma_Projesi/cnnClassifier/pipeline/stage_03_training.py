from src.cnnClassifier.config.configration import ConfigurationManager
from src.cnnClassifier.components.prepare_callbacks import PrepareCallback
from src.cnnClassifier.components.training import Training
from src.cnnClassifier import logger

STAGE_NAME = "Training"  # Aşama ismi

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Konfigürasyon yöneticisini oluştur
        config = ConfigurationManager()
        # Geri çağırma konfigürasyonunu al
        prepare_callbacks_config = config.get_prepare_callback_config()
        # Geri çağırmaları ayarla
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()  # TensorBoard ve checkpoint geri çağırmalarını al

        # Eğitim konfigürasyonunu al
        training_config = config.get_training_config()
        # Eğitim sınıfını başlat
        training = Training(config=training_config)
        training.get_base_model()  # Temel modeli yükle
        training.train_valid_generator()  # Eğitim ve doğrulama veri jeneratörlerini hazırla
        # Modeli eğit
        training.train(callback_list=callback_list)

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat