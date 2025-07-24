import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib
matplotlib.use('TkAgg')    
import matplotlib.pyplot as plt
import requests
from io import BytesIO #bytes io is used for buffer memory to stoe or capture imgs

def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content)) 

rs6_url="https://www.topgear.com/sites/default/files/2024/07/6-Audi-RS6-Avant-GT-US-review-2024.jpg?w=1784&h=1004"
#cls_url="https://www.platinumautohaus.com/imagetag/13024/3/l/Used-2013-Mercedes-Benz-CLS63-AMG-***-AMG-PERFORMANCE-PACKAGE-**.jpg"

rs6 = load_image_from_url(rs6_url)
#cls6= load_image_from_url(cls_url)

#display original image
plt.figure(figsize=(10,6))
plt.imshow(rs6)
plt.title("Audi RS6 Avant GT")
plt.axis('off')  # Hide axes
plt.show()

#image to array
rs6_array = np.array(rs6)
print("Image shape:", rs6_array.shape)

#grayscale img
rs6_gray = rs6.convert("L")  # Convert to grayscale
plt.figure(figsize=(10,6))
plt.imshow(rs6, cmap='gray')
plt.title("Audi RS6 Avant GT - Grayscale")
plt.axis('off')  # Hide axes 
plt.show()
