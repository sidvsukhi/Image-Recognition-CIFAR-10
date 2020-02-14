from keras.models import model_from_json
from pathlib import Path
from keras.preprocessing import image
import numpy as np


class_labels=[
	"Plane",
	"Car",
	"Bird",
	"Cat",
	"Deer",
	"Dog",
	"Frog",
	"Horse",
	"Horse",
	"Boat",
	"Truck"
]

#load json of model structure
f=Path("model_structure.json")
model_structure=f.read_text()

#recreate keras model from json
model=model_from_json(model_structure)

#load weights into model
model.load_weights("model_weights.h5")

#load image to test
img=image.load_img("frog.jpg",target_size=(32,32))

#convert img to numpy array
image_to_test=image.img_to_array(img)/255

#add dimension
list_of_images=np.expand_dims(image_to_test,axis=0)

#predict
results=model.predict(list_of_images)

#since single image so only first element
single_result=results[0]

#likelihood score of all 10 classes
most_likely_class_index=int(np.argmax(single_result))
class_likelihood=single_result[most_likely_class_index]

#class label of the predicted image
class_label=class_labels[most_likely_class_index]

print("This is image is a {} - Likelihood: {:2f}".format(class_label,class_likelihood))
