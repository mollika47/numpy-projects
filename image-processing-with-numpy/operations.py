from PIL import Image
import numpy as np

img = np.array(Image.open("image/GTA VI(original).jpg"))

def inspect_image():
    print("\nImage Properties:")
    h, w, c = img.shape
    print(f"Dimension: {img.ndim}D")
    print(f"Resolution: {w}x{h}")
    print(f"Channels: {c}")

def pixel_analysis():
    print("\npixel analysis:")
    print("Data Type:", img.dtype)
    print("Minimum pixel value:", np.min(img))
    print("Maximum pixel value:", np.max(img))
    print("Average pixel value:", np.round(np.mean(img), 2))

def save_image(op):
    name = input("File name: ")
    Image.fromarray(op).save(f"image/user saved/{name}.jpg")
    print("Image saved!")

def crop_image():
    h, w, c = img.shape
    center_x = w // 2
    center_y = h // 2

    print("\nCenter Square Image: 1")
    print("Top-half Image: 2")
    print("Bottom-half Image: 3")
    print("Left-half Image: 4")
    print("Right-half Image: 5")
    print("Manual (%): 6")

    cp = int(input("Choose position: "))

    if cp == 1:
        center_sqr = img[(center_y-500):(center_y+500), (center_x-500):(center_x+500)]
        Image.fromarray(center_sqr).show()
        save = input("Save image? (y/n): ")
        if save == "y":
            save_image(center_sqr)

    elif cp == 2:
        top_half = img[:center_y, :]
        Image.fromarray(top_half).show()
        save = input("Save image? (y/n): ")
        if save == "y":
            save_image(top_half)

    elif cp == 3:
        bottom_half = img[center_y:, :]
        Image.fromarray(bottom_half).show()
        save = input("Save image? (y/n): ")
        if save == "y":
            save_image(bottom_half)

    elif cp == 4:
        left_half = img[:, :center_x]
        Image.fromarray(left_half).show()
        save = input("Save image? (y/n): ")
        if save == "y":
            save_image(left_half)

    elif cp == 5:
        right_half = img[:, center_x:]
        Image.fromarray(right_half).show()
        save = input("Save image? (y/n): ")
        if save == "y":
            save_image(right_half)

    elif cp == 6:
        percents = int(input("Enter percents (%): "))
        crop = img[:int(h * (percents / 100)), :int(w * (percents / 100))]
        Image.fromarray(crop).show()
        save = input("Save image? (y/n): ")
        if save == "y":
            save_image(crop)

    else:
        print("Invalid input!")