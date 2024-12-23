from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin # Flask uygulamamızın farklı kaynaklar arasında geçiş yapmamızı sağlar. Yani Farklı Apilere erişim sağlar
from src.cnnClassifier.utils.common import decodeImage 
from src.cnnClassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF8')

app = Flask(__name__)
CORS(app) # farklı alanlardan gelen apiler FLASK API'MIZE ERIŞIM SAĞLAYABİLİYOR


class ClientApp:
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = PredictionPipeline(self.filename)


@app.route('/', methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return 'Eğitim Başarıyla Tamamlandı'

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clapp.filename) #array formatına dönüştür
    result = clapp.classifier.predict() # tahminlemeyi çalıştırdım
    return jsonify(result) #sonucu sözlük formatına jsonify() methoduyla dönüştürdüm

if __name__ == '__main__':
    clapp = ClientApp()
    app.run(host = '0.0.0.0', port = 8080)

