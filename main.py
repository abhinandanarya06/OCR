import cv2
import tensorflow as tf
from ocr_help import *






model = tf.keras.models.load_model('model.h5')
text_detector= tf.keras.Sequential(
    model,
    tf.keras.layers.Softmax()
)

imgs = [f for f in os.listdir('.') if f.endswith('.jpg')]
img_no = 0
for img in imgs:
    print('*'*30, 'Text on {}'.format(img), '*'*30)
    img = cv2.imread(img)
    TEXT = apply_ocr(img)
    imshow(img)
    print(TEXT)
    print('-'*80, '\n\n')
    img_no += 1
