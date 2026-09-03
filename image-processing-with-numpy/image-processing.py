from PIL import Image
import numpy as np

img = np.array(Image.open("image/GTA VI(original).jpg"))
print(img)

def inspect_image():
    print("Image Properties:")
    h, w, c = img.shape
    print(f"Dimension: {img.ndim}D")
    print(f"Resolution: {w}x{h}")
    print(f"Channels: {c}")

def pixel_analysis():
    print("pixel analysis:")
    print("Data Type:", img.dtype)
    print("Minimum pixel value:", np.min(img))
    print("Maximum pixel value:", np.max(img))
    print("Average pixel value:", np.round(np.mean(img), 2))
    px = img[:1080, :1920]
    print(f"px: {px}")
    Image.fromarray(px).show()

inspect_image()
pixel_analysis()


# arr = img.reshape()
# print(arr)