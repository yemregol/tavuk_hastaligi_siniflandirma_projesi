import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename  # Tahmin edilecek görüntü dosyasını al

    def predict(self):
        # Modeli yükle
        model = load_model(os.path.join('artifacts', 'training', 'model.keras'))  # artifacts/training/model.keras
        imagename = self.filename
        
        # Görüntüyü yükle ve boyutlandır
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)  # Modelin piksel değerleri ile tahmin yapması için dizi formatına dönüştür
        test_image = np.expand_dims(test_image, axis=0)  # 4D şekline getir (1, 224, 224, 3)
        
        # Tahmin yap
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        # Sonuçları değerlendir ve tahmin yap
        if result[0] == 1:
            prediction = 'Healthy'  # Sağlıklı olarak tahmin et
            return [{'prediction': prediction}]
        else:
            prediction = 'Cocidiosis'  # Cocidiosis olarak tahmin et
            return [{'prediction': prediction}]