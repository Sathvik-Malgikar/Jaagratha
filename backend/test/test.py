import cv2
from tensorflow import keras
import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
import numpy as np


crimeDetector = keras.models.load_model(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\crime_detect_modelH5.h5')
# img1 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\1.jpg')
# img2 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\2.jpg')
# img3 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\3.jpg')
# img4 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\4.jpg')
# img5 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\5.jpg')
# img6 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\6.jpg')
# img7 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\7.jpg')
# img8 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\8.jpg')
# img9 = cv2.imread(r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\9.jpg')

# l = []
# l.append(tf.expand_dims(img1, axis=0))
# l.append(tf.expand_dims(img2, axis=0))
# l.append(tf.expand_dims(img3, axis=0))
# l.append(tf.expand_dims(img4, axis=0))
# l.append(tf.expand_dims(img5, axis=0))
# l.append(tf.expand_dims(img6, axis=0))
# l.append(tf.expand_dims(img7, axis=0))
# l.append(tf.expand_dims(img8, axis=0))
# l.append(tf.expand_dims(img9, axis=0))


preprocess_fun = tf.keras.applications.densenet.preprocess_input
train_dir = r'C:\Users\prana\Desktop\Workspaces\Hack Attack\Jaagratha\backend\test\imgs'

final_gen = ImageDataGenerator(horizontal_flip=True,
                                   width_shift_range=0.1,
                                   height_shift_range=0.05,
                                   rescale = 1./255,
                                   preprocessing_function=preprocess_fun
                                  )
final_gen2 = final_gen.flow_from_directory(directory = train_dir,
                                                    target_size = (64, 64),
                                                    batch_size = 1,
                                                    shuffle  = True , 
                                                    color_mode = "rgb",
                                                    class_mode = "categorical",
                                                    seed = 10,
                                                    classes = ['Abuse','Arrest','Arson','Assault','Burglary','Explosion','Fighting',"Normal",'RoadAccidents','Robbery','Shooting','Shoplifting','Stealing','Vandalism']
                                                   )

classes = ['Abuse','Arrest','Arson','Assault','Burglary','Explosion','Fighting',"Normal",'RoadAccidents','Robbery','Shooting','Shoplifting','Stealing','Vandalism']

pred_val = crimeDetector.predict(final_gen2, verbose=1)
predicted_class = np.argmax(crimeDetector.predict(final_gen2), axis=-1)
# i = pred_val.index(predicted_class)
# print()
probabilities = predicted_class.tolist()
actual_probabilities = [np.max(vector) for vector in pred_val]
classes_for_img = [classes[list(vector).index(np.max(vector))] for vector in pred_val]
print(classes_for_img)
# cv2.imshow("test", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()