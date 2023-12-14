from time import time
import os
import cv2
import tensorflow as tf
import numpy as np
import keras.utils as image
import json
from PIL import Image


labels={0: 'Cardboard', 1: 'Glass', 2: 'Metal', 3: 'Paper', 4: 'Plastic', 5: 'Trash'}
img_path = 'C:\\Users\\Prakash\\Desktop\\internship\\Waste_Segregation\\plastic1.jpg'
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