from detecto.core import Model
from detecto import utils, visualize
from detecto.core import Dataset


# If your images and labels are in separate folders
dataset = Dataset('/Users/mahesh/mltrain/')

from detecto.visualize import show_labeled_image

image, targets = dataset[0]
#show_labeled_image(image, targets['boxes'], targets['labels'])

your_labels = ['malu']
model = Model(your_labels)

model.fit(dataset, verbose=True)