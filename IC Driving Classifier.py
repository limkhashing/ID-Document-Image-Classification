import numpy as np

from keras.preprocessing import image
from keras.models import load_model

IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_CHANNELS = 3
INPUT_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)

model = load_model('./model/model.h5')

test_image = image.load_img('./dataset_v2/single_prediction/test-2.jpg', target_size = INPUT_SHAPE)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)

if result[0][0] == 1:
    prediction = 'ic'
else:
    prediction = 'driving'

print(prediction)