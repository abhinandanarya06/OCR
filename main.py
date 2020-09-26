import cv2
import tensorflow as tf
from ocr_help import *
import os
import numpy as np

## LOADING MODEL IN CURRENT DIRECTORY NAMED model.h5 FILE
model = tf.keras.models.load_model('model.h5')

## GETTING IMAGE FILE FROM CURRENT DIRECTORY
test_images_path = 'sample_test_image/'
imgs = [f for f in os.listdir(test_images_path)]
img_no = 0

## APPLYING OCR ON EVERY IMAGE FILE AND SHOWING RESULTS
for img in imgs:
    print('*'*30, 'Text on {}'.format(img), '*'*30)
    img = cv2.imread(test_images_path + img, 0)
    TEXT = apply_ocr(img, model)
    print(TEXT)
    print('-'*80, '\n\n')
    img_no += 1
