# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:58:57 2021

@author: arany
"""


import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps

sign_names = {
        0: 'Speed limit (20km/h)',
        1: 'Speed limit (30km/h)',
        2: 'Speed limit (50km/h)',
        3: 'Speed limit (60km/h)',
        4: 'Speed limit (70km/h)',
        5: 'Speed limit (80km/h)',
        6: 'End of speed limit (80km/h)',
        7: 'Speed limit (100km/h)',
        8: 'Speed limit (120km/h)',
        9: 'No passing',
        10: 'No passing for vehicles over 3.5 metric tons',
        11: 'Right-of-way at the next intersection',
        12: 'Priority road',
        13: 'Yield',
        14: 'Stop',
        15: 'No vehicles',
        16: 'Vehicles over 3.5 metric tons prohibited',
        17: 'No entry',
        18: 'General caution',
        19: 'Dangerous curve to the left',
        20: 'Dangerous curve to the right',
        21: 'Double curve',
        22: 'Bumpy road',
        23: 'Slippery road',
        24: 'Road narrows on the right',
        25: 'Road work',
        26: 'Traffic signals',
        27: 'Pedestrians',
        28: 'Children crossing',
        29: 'Bicycles crossing',
        30: 'Beware of ice/snow',
        31: 'Wild animals crossing',
        32: 'End of all speed and passing limits',
        33: 'Turn right ahead',
        34: 'Turn left ahead',
        35: 'Ahead only',
        36: 'Go straight or right',
        37: 'Go straight or left',
        38: 'Keep right',
        39: 'Keep left',
        40: 'Roundabout mandatory',
        41: 'End of no passing',
        42: 'End of no passing by vehicles over 3.5 metric tons'}

def import_and_predict(image_data, model):
    
        size = (32,32)    
        image = ImageOps.fit(image_data,(100, 100), size, Image.ANTIALIAS)
        image = image.convert('RGB')
        image = np.asarray(image)
        img_reshape = image[np.newaxis,...]

        prediction = model.predict_classes(img_reshape)
        
        return prediction

model = tf.keras.models.load_model(r"C:\Users\arany\Downloads\Model\traffic_sign.h5")

st.write("""  Traffic Sign Prediction   """ )

#st.write("This is a simple image classification web app to predict rock-paper-scissor hand sign")

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
#
if file is None:
    st.text(" ")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    #prediction = import_and_predict(image, model)
    if st.button('predict'):
        st.write("Result...")
        label = import_and_predict(image, model)
        #st.write(label )
        label = label.item()
        res = sign_names.get(label)
        st.markdown(res)