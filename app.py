from flask import Flask, render_template

from time import time
import os
import cv2
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import json
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')

def predict(img_path):
     
     labels={0: 'Cardboard', 1: 'Glass', 2: 'Metal', 3: 'Paper', 4: 'Plastic', 5: 'Trash'}
     img_path = '../platic3.jpg'
     img = image.load_img(img_path, target_size=(32,32))
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
     print("classified label:",predicted_class)
     result=''
     if predicted_class in ['Cardboard','Paper']:
          category = "Biodegradable"
          predicted_class = str(predicted_class)
          probability = str(prob)
          return category, predicted_class,probability
          
     elif predicted_class in ['Metal','Glass','Plastic']:
          category = "Non-Biodegradable"
          predicted_class = str(predicted_class)
          probability = str(prob)
          return category,predicted_class,probability
        
     else:
          category = "Categorizing Difficult"
          predicted_class = str(predicted_class)
          probability = str(prob)
          return category, predicted_class, probability
          #result = predicted_class + '\n' + str(pro)
     #return(result)
#category,predicted_class,probability = predict(Image_path)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

    #on clicking upload, display image and call predict function, and display the output