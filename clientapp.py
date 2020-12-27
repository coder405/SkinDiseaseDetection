import flask
import os
from predict import Skin_disease_detection
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
CORS(app)


class clientapp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = Skin_disease_detection(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['GET'])
@cross_origin()
def PredictRoute():
    image = request.json['image']
    #decodeImage(image, clApp.filename)
    result = clApp.classifier.predictSkinDisease()
    return jsonify(result)

clApp = clientapp()

port = (os.getenv("PORT")
    #app.run(host='0.0.0.0', port=port)
app.run(host = '0.0.0.0', port = 8000, debug = True)
