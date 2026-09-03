from PIL import Image
import numpy as np

img = np.array(Image.open("image/GTA VI(original).jpg"))

def inspect_image():
    print("Image Properties:")
    h, w, c = img.shape
    print(f"Dimension: {img.ndim}D")
    print(f"Resolution: {w}x{h}")
    print(f"Channels: {c}")

inspect_image()