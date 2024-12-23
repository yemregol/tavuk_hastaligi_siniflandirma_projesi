import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time

from src.cnnClassifier.entity.config_entity import PrepareCallbacksConfig
                                                
class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config  # Yapılandırma dosyasını yükle

    @property
    def _create_tb_callbacks(self):
        # TensorBoard için zaman damgası ile kayıt dizini oluştur
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)  # TensorBoard callback'i döndür

    @property
    def _create_ckpt_callbacks(self):
        # En iyi modeli kaydeden checkpoint callback'i döndür
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    def get_tb_ckpt_callbacks(self):
        # TensorBoard ve Checkpoint callback'lerini döndür
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]