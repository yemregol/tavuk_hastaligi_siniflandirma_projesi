from src.cnnClassifier.config.configration import ConfigurationManager
from src.cnnClassifier.components.evaluation import Evaluation
from src.cnnClassifier import logger

STAGE_NAME = "Evaluation stage"  # Değerlendirme aşaması ismi

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        # Konfigürasyon yöneticisini oluştur
        config = ConfigurationManager()
        # Değerlendirme konfigürasyonunu al
        val_config = config.get_validation_config()
        # Değerlendirme sınıfını başlat
        evaluation = Evaluation(val_config)
        evaluation.evaluation()  # Modeli değerlendir
        evaluation.save_score()  # Sonuçları kaydet

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        # Aşamanın başladığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()  # Pipeline nesnesini oluştur
        obj.main()  # Ana fonksiyonu çalıştır
        # Aşamanın tamamlandığını kaydet
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)  # Hata durumunda kaydet
        raise e  # Hata fırlat