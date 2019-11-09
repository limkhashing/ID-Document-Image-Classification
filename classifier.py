import numpy as np

from keras.preprocessing import image
from keras.models import load_model

IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_CHANNELS = 3
INPUT_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)
prediction = ''

# model v2 is binary classifier
# {'driving_license': 0, 'identity_card': 1}
# model = load_model('./model/model_v2.h5')

# model v3 is multi-class classifier
# {'driving_license': 0, 'identity_card': 1, 'passport': 2}
model = load_model('./model/model_v3.h5')

test_image = image.load_img('./dataset_v3/single_prediction/test driving.jpg', target_size = INPUT_SHAPE)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
result = np.argmax(result[0])

print(result)

# if result == 0:
#     prediction = 'driving'
# elif result == 1:
#     prediction = 'ic'

if result == 0:
    prediction = 'driving_license'
elif result == 1:
    prediction = 'identity_card'
elif result == 2:
    prediction = 'passport'

print(prediction)