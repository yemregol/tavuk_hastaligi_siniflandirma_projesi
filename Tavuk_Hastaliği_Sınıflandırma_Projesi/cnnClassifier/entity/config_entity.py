from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:  # Veri Alımı Yapılandırması
    root_dir: Path  # Ana dizin
    source_URL: str  # Veri URL'si
    local_data_file: Path  # Yerel veri dosyası
    unzip_dir: Path  # Çıkartılacak dizin

@dataclass(frozen=True)
class PrepareBaseModelConfig:  # Temel Model Hazırlığı Yapılandırması
    root_dir: Path  # Ana dizin
    base_model_path: Path  # Temel model yolu
    updated_base_model_path: Path  # Güncellenmiş model yolu
    params_image_size: list  # Görüntü boyutu parametresi
    params_learning_rate: float  # Öğrenme hızı
    params_include_top: bool  # Üst katman dahil etme durumu
    params_weights: str  # Ağırlık türü
    params_classes: int  # Sınıf sayısı

@dataclass(frozen=True)
class PrepareCallbacksConfig:  # Callback Hazırlığı Yapılandırması
    root_dir: Path  # Ana dizin
    tensorboard_root_log_dir: Path  # TensorBoard log dizini
    checkpoint_model_filepath: Path  # Checkpoint model yolu

@dataclass(frozen=True)
class TrainingConfig:  # Eğitim Yapılandırması
    root_dir: Path  # Ana dizin
    trained_model_path: Path  # Eğitilmiş model yolu
    updated_base_model_path: Path  # Güncellenmiş model yolu
    training_data: Path  # Eğitim verisi yolu
    params_epochs: int  # Epoch sayısı
    params_batch_size: int  # Batch boyutu
    params_is_augmentation: bool  # Veri artırma durumu
    params_image_size: list  # Görüntü boyutu

@dataclass(frozen=True)
class EvaluationConfig:  # Değerlendirme Yapılandırması
    path_of_model: Path  # Model yolu
    training_data: Path  # Eğitim verisi yolu
    all_params: dict  # Tüm parametreler
    params_image_size: list  # Görüntü boyutu
    params_batch_size: int  # Batch boyutu