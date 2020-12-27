import numpy as np
from keras.models import load_model
from keras.preprocessing import image


class Skin_disease_detection:
    def __init__(self, filename):
        self.filename = filename

    def predictSkinDisease(self):
        model = load_model('skin_disease_detection_model.h5')

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)

        if result[0][0] == 0:
            prediction = "melanoma"
            return [{"image": prediction}]

        elif result[0][0] == 1:
            prediction = "nevus"
            return [{"image": prediction}]

        elif result[0][0] == 2:
            prediction = "seborrheic_keratosis"
            return [{"image": prediction}]
