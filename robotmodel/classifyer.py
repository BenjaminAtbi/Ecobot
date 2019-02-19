import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

class classifyer:


    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def classifyimage(self,image):
        return self.client.label_detection(image=image)

# Instantiates a client


# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    '..\\testimages\\G05.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
l = classifyer()

print("l:",l,"stuff:",l.classifyimage(image))