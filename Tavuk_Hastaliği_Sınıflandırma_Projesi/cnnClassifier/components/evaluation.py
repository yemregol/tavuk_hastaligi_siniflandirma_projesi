import tensorflow as tf
from pathlib import Path
from src.cnnClassifier.entity.config_entity import EvaluationConfig
from src.cnnClassifier.utils.common import save_json

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config  # Yapılandırma dosyasını yükle

    def _valid_generator(self):
        # Doğrulama veri seti için parametreler
        datagenerator_kwargs = dict(
            rescale=1./255,  # Piksel değerlerini ölçeklendir
            validation_split=0.30  # Veriyi %30 doğrulama seti olarak ayır
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],  # Hedef boyut
            batch_size=self.config.params_batch_size,  # Batch boyutu
            interpolation="bilinear"  # Görüntü interpolasyonu
        )

        # Doğrulama veri jeneratörünü oluştur
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        # Doğrulama veri akışını başlat
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)  # Modeli verilen yoldan yükle

    def evaluation(self):
        model = self.load_model(self.config.path_of_model)  # Modeli yükle
        self._valid_generator()  # Doğrulama veri setini hazırla
        self.score = model.evaluate(self.valid_generator)  # Modeli değerlendir

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}  # Sonuçları al
        save_json(path=Path("scores.json"), data=scores)  # Sonuçları JSON dosyasına kaydet