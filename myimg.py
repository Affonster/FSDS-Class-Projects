import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import warnings

# Suppress matplotlib warnings
warnings.filterwarnings("ignore")

# Set Streamlit page config
st.set_page_config(page_title="RS6", layout="wide")

# Title
st.title("GTA 6 Image - Multi-Color Channel Visualizer")

# Load image from local path
@st.cache_data
def load_image():
    path = r"C:\Users\Affan\OneDrive\Desktop\Beauty\May 26 2026.jpg"
    return Image.open(path).convert("RGB")

# Load and display image
rs6 = load_image()
st.image(rs6, caption="Original RS6 Image", use_container_width=True)

# Convert to NumPy array
rs6_np = np.array(rs6)
R, G, B = rs6_np[:, :, 0], rs6_np[:, :, 1], rs6_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(rs6_np)
green_img = np.zeros_like(rs6_np)
blue_img = np.zeros_like(rs6_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

rs6_gray = rs6.convert("L")
rs6_gray_np = np.array(rs6_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
ax.imshow(rs6_gray_np, cmap=colormap)
plt.axis("off")

# Display plot in Streamlit
st.pyplot(fig)
