from PIL import Image
import numpy as np

img = np.array(Image.open("image/GTA VI(original).jpg"))

def inspect_image():
    print("Image Properties:")
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

# def crop_image():
#     h, w, c = img.shape
#     center_x = w // 2
#     center_y = h // 2
#
#     center_sqr = img[(center_y-500):(center_y+500), (center_x-500):(center_x+500)]
#     Image.fromarray(center_sqr).show()
#
#     top_half = img[:center_y, :]
#     Image.fromarray(top_half).show()
#
#     bottom_half = img[center_y:, :]
#     Image.fromarray(bottom_half).show()
#
#     left_half = img[:, :center_x]
#     Image.fromarray(left_half).show()
#
#     right_half = img[:, center_x:]
#     Image.fromarray(right_half).show()
#
#     top_25 = img[:int(h * 0.25), :]
#     Image.fromarray(top_25).show()
#
#     bottom_left_30 = img[int(h * 0.3):, :int(w * 0.3)]
#     Image.fromarray(bottom_left_30).show()
#
#     right_65 = img[:, int(w * 0.35):]
#     Image.fromarray(right_65).show()

# def grayscale():
#     gray = np.mean(img, axis=2).astype(np.uint8)
#     Image.fromarray(gray).save("image/GTA VI(grayscale).jpg")

# def adjustments(amount):
#     bright = np.clip(img.astype(np.uint16) + amount, 0, 255).astype(np.uint8)
#     Image.fromarray(bright).save("image/GTA VI(brighter).jpg")
#
#     darker = np.clip(img.astype(np.int16) - amount, 0, 255).astype(np.uint8)
#     Image.fromarray(darker).save("image/GTA VI(darker).jpg")

# def inverted():
#     neg = 255 - img
#     Image.fromarray(neg).save("image/GTA VI(original-to-inverted).jpg")
#     ori = np.array(Image.open("image/GTA VI(grayscale).jpg"))
#     neg_g = 255 - ori
#     Image.fromarray(neg_g).save("image/GTA VI(grayscale-to-inverted).jpg")

# def threshold():
#     loaded_img = np.array(Image.open("image/GTA VI(grayscale).jpg"))
#     threshold_point = 128
#     t_img = np.where(loaded_img > threshold_point, 255, 0).astype(np.uint8)
#     Image.fromarray(t_img).save("image/GTA VI(threshold).jpg")

# def resize():
#     full_hd = img[::2, ::2]
#     print("\nresized to ", full_hd.shape)
#     Image.fromarray(full_hd).save("image/GTA VI(res_full-HD).jpg")
#
#     hd = img[::3, ::3]
#     print("\nresized to ", hd.shape)
#     Image.fromarray(hd).save("image/GTA VI(res_HD).jpg")

def flip_image():
    vertical_flip = np.flip(img, axis=0)
    Image.fromarray(vertical_flip).save("image/flipped_vertical.jpg")

    horizontal_flip = np.flip(img, axis=1)
    Image.fromarray(horizontal_flip).save("image/flipped_horizontal.jpg")

inspect_image()
pixel_analysis()
# crop_image()
# grayscale()
# adjustments(50)
# inverted()
# threshold()
# resize()
flip_image()


