from flask import Flask, render_template, request, jsonify

from time import time
import os
import cv2
import tensorflow as tf
import numpy as np
import keras.utils as image
import json
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder='template')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
     labels={0: 'Cardboard', 1: 'Glass', 2: 'Metal', 3: 'Paper', 4: 'Plastic', 5: 'Trash'}

     if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

     file = request.files['image']

     if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the uploaded image
     filename = secure_filename(file.filename)
     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
     file.save(file_path)

     #img_path = 'C:\\Users\\Prakash\\Desktop\\internship\\Waste_Segregation\\plastic1.jpg'
     img = image.load_img(file_path, target_size=(32,32))
     img = image.img_to_array(img, dtype=np.uint8)
     img = np.array(img)/255.0
     model = tf.keras.models.load_model("model1.h5")

     predicted = model.predict(img[np.newaxis, ...])
     prob = np.max(predicted[0], axis=-1)
     prob = prob*100
     prob = round(prob,2)
     prob = str(prob) + '%'
     print("p.shape:",predicted.shape)
     print("prob",prob)
     predicted_class = labels[np.argmax(predicted[0], axis=-1)]
     print("Classified label:",predicted_class)
     return jsonify({'prediction': predicted_class, 'probability': f'{prob}'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

    #on clicking upload, display image and call predict function, and display the output