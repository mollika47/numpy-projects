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

def save_image(file):
    msg = input("Save image? (y/n): ")

    if msg == "y":
        name = input("File name: ")
        Image.fromarray(file).save(f"image/user saved/{name}.jpg")
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
        save_image(center_sqr)

    elif cp == 2:
        top_half = img[:center_y, :]
        Image.fromarray(top_half).show()
        save_image(top_half)

    elif cp == 3:
        bottom_half = img[center_y:, :]
        Image.fromarray(bottom_half).show()
        save_image(bottom_half)

    elif cp == 4:
        left_half = img[:, :center_x]
        Image.fromarray(left_half).show()
        save_image(left_half)

    elif cp == 5:
        right_half = img[:, center_x:]
        Image.fromarray(right_half).show()
        save_image(right_half)

    elif cp == 6:
        percents = int(input("Enter percents (%): "))
        crop = img[:int(h * (percents / 100)), :int(w * (percents / 100))]
        Image.fromarray(crop).show()
        save_image(crop)

    else:
        print("Invalid input!")

def grayscale():
    gray = np.mean(img, axis=2).astype(np.uint8)
    Image.fromarray(gray).show()
    return gray

def inverted():
    neg = 255 - img
    Image.fromarray(neg).show()
    return neg

def threshold():
    loaded_img = np.array(Image.open("image/demo/GTA VI(grayscale).jpg"))
    threshold_point = 128
    t_img = np.where(loaded_img > threshold_point, 255, 0).astype(np.uint8)
    Image.fromarray(t_img).show()
    return t_img

def filters():
    print("Type g for Grayscale Image")
    print("Type i for Inverted Image")
    print("Type t for threshold Image")

    choice = input("Type : ")

    if choice.lower() == "g":
        g = grayscale()
        save_image(g)
    elif choice.lower() == "i":
        i = inverted()
        save_image(i)
    elif choice.lower() == "t":
        t = threshold()
        save_image(t)
    else:
        print("Invalid input!")

def adjustments():
    print("To increase brightness: 1")
    print("To decrease brightness: 2")

    choice = input("Type : ")

    if choice == "1":
        amount = int(input("Enter amount: "))
        bright = np.clip(img.astype(np.uint16) + amount, 0, 255).astype(np.uint8)
        Image.fromarray(bright).show()
        save_image(bright)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        dark = np.clip(img.astype(np.int16) - amount, 0, 255).astype(np.uint8)
        Image.fromarray(dark).show()
        save_image(dark)

    else:
        print("Invalid input!")

def resize():
    print("Image will be resized to 1080p and 720p")
    full_hd = img[::2, ::2]
    Image.fromarray(full_hd).show()
    save_image(full_hd)

    hd = img[::3, ::3]
    Image.fromarray(hd).show()
    save_image(hd)

def flip_image():
    print("Image will be flipped vertically and horizontally")

    vertical_flip = np.flip(img, axis=0)
    Image.fromarray(vertical_flip).show()
    save_image(vertical_flip)

    horizontal_flip = np.flip(img, axis=1)
    Image.fromarray(horizontal_flip).show()
    save_image(horizontal_flip)

