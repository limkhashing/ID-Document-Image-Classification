import numpy as np

from keras.preprocessing import image
from keras.models import load_model

IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128
IMAGE_CHANNELS = 3
INPUT_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)

class_names = ["Driving License", "Identity Card", "Passport"]

# model v2 is binary classifier
# {'driving_license': 0, 'identity_card': 1}
model = load_model('./model/model_v2.h5')

# model v3 is multi-class classifier
# {'driving_license': 0, 'identity_card': 1, 'passport': 2}
# model = load_model('./model/model_v3.h5')

test_image = image.load_img('./dataset_v3/single_prediction/test driving.jpg', target_size = INPUT_SHAPE)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
probability = model.predict(test_image)
prediction = np.argmax(probability[0])

print("Probability: ", probability)
print("Prediction: ", prediction)
print("Prediction class: ", class_names[int(prediction)])
