from src.cnnClassifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config  # Yapılandırma dosyasını yükle
    
    def get_base_model(self):
        # Güncellenmiş modeli yükle
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
    
    def train_valid_generator(self):
        # Veriyi ölçeklendirme ve doğrulama bölmesi ayarları
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        # Veri akışı ayarları
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        # Doğrulama veri üreticisini oluştur
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        # Eğer artırma yapılacaksa, eğitim veri üreticisini oluştur
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        # Eğitim veri üreticisini oluştur
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        # Modeli belirtilen yola kaydet
        model.save(path)

    def train(self, callback_list: list):
        # Eğitim adım sayısını ve doğrulama adım sayısını hesapla
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        # Modeli eğit
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        # Eğitilmiş modeli kaydet
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )