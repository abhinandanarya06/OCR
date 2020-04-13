import cv2
import tensorflow as tf
from ocr_help import *
import os
import numpy as np

## LOADING MODEL IN CURRENT DIRECTORY NAMED model.h5 FILE
model = tf.keras.models.load_model('model.h5')

## ADDING SOFTMAX ACTIVATION
text_detector= tf.keras.Sequential(
    model,
    tf.keras.layers.Softmax()
)

## GETTING IMAGE FILE FROM CURRENT DIRECTORY
imgs = [f for f in os.listdir('.') if f.endswith('.jpg')]
img_no = 0

## APPLYING OCR ON EVERY IMAGE FILE AND SHOWING RESULTS
for img in imgs:
    print('*'*30, 'Text on {}'.format(img), '*'*30)
    img = cv2.imread(img)
    TEXT = apply_ocr(img, text_detector)
    cv2.imshow('window', img)
    print(TEXT)
    print('-'*80, '\n\n')
    img_no += 1
