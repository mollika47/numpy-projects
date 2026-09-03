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

def crop_image():
    h, w, c = img.shape
    center_x = w // 2
    center_y = h // 2
    center_sqr = img[(center_y-500):(center_y+500), (center_x-500):(center_x+500)]
    Image.fromarray(center_sqr).show()

    top_half = img[:center_y, :]
    Image.fromarray(top_half).show()

    bottom_half = img[center_y:, :]
    Image.fromarray(bottom_half).show()

    left_half = img[:, :center_x]
    Image.fromarray(left_half).show()

    right_half = img[:, center_x:]
    Image.fromarray(right_half).show()



inspect_image()
pixel_analysis()
crop_image()
