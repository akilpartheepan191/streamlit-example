import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image, ImageOps
import numpy as np
from CaptureImage import *


def teachable_machine_classification(img, file):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = keras.models.load_model(file)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img
    # image = Image.open(img_name).convert('RGB')
    # image = cv2.imread(image)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    #print(prediction)
    return np.argmax(prediction)


st.title("AI Police welcomes you back to school!")
st.header("Mask up or get caught by the police!")
st.text("Always wear your mask to help contain covid-19.")
st.button('Click Me, I shall photograph you to check', key='button_photograph',
          on_click=captureImageFunction)

# file upload and handling logic
#uploaded_file = st.file_uploader("Upload your JPEG image here,and i will tell you if you are wearing a mask or not", type="jpeg")
#if uploaded_file is not None:
    #image = Image.open(uploaded_file).convert('RGB')
img_name = 'CapturedFrame0.jpg'
image = Image.open(img_name).convert('RGB')
st.image(image, caption='Caught your image.', use_column_width=True)
st.write("")
st.write("Verifying with my Artificial Intelligence...")
label = teachable_machine_classification(image, 'keras_model.h5')
if label == 1:
   st.write("hmph!Why are'nt you wearing your mask... wear it immediately... or i will call the cops!")
else:
        st.write("Good job! You are wearing a mask. Do wear your mask always.")
