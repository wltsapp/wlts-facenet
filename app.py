import time
import os
import random
from flask import Flask, render_template, request
from glob import glob
from pprint import pprint
import json

#from lib import nn
from lib import face

app = Flask(__name__)
predictor = None

def initialize():
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # 10MiB
    global predictor
    if not predictor:
        predictor = face.Predictor()

@app.route('/')
def index():
    initialize()
    return render_template('index.html')

@app.route('/preprocess')
def preprocess():
    initialize()
    from packages import preprocess
    return render_template('train.html')

@app.route('/classifier')
def classifier():
    initialize()
    from packages import classifier
    return render_template('train.html')

@app.route('/train')
def train():
    initialize()
    from packages import train_main
    return render_template('train.html')
    
@app.route('/upload', methods=['POST'])
def upload():
    initialize()
    upfile = request.files["upfile"]
    img_file = "image" + str(random.randint(0, 999999)) + os.path.splitext(upfile.filename)[1]
    img_path = os.path.join("./cache/", img_file)
    img_path1 = os.path.join("./test/", img_file)
    print(img_path);
    upfile.save(img_path)
    upfile.save(img_path1)
    item = predictor.get_image_item(img_path1)    
    #os.remove(img_path)
    return json.dumps(item)

if __name__ == '__main__':
    app.run()
