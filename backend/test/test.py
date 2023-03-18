import cv2
from tensorflow import keras
import tensorflow as tf

crimeDetector = keras.models.load_model(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\crime_detect_modelH5.h5')
img1 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\1.jpg')
img2 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\2.jpg')
img3 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\3.jpg')
img4 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\4.jpg')
img5 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\5.jpg')
img6 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\6.jpg')
img7 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\7.jpg')
img8 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\8.jpg')
img9 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\9.jpg')

l = []
l.append(tf.expand_dims(img1, axis=0))
l.append(tf.expand_dims(img2, axis=0))
l.append(tf.expand_dims(img3, axis=0))
l.append(tf.expand_dims(img4, axis=0))
l.append(tf.expand_dims(img5, axis=0))
l.append(tf.expand_dims(img6, axis=0))
l.append(tf.expand_dims(img7, axis=0))
l.append(tf.expand_dims(img8, axis=0))
l.append(tf.expand_dims(img9, axis=0))
pred_val = crimeDetector.predict(l)
print(pred_val)

cv2.imshow("test", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()