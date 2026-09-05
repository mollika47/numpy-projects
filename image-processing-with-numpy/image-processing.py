from operations import *



#

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

# def flip_image():
#     vertical_flip = np.flip(img, axis=0)
#     Image.fromarray(vertical_flip).save("image/flipped_vertical.jpg")
#
#     horizontal_flip = np.flip(img, axis=1)
#     Image.fromarray(horizontal_flip).save("image/flipped_horizontal.jpg")

# def rotate_image():
#     rotate1 = np.rot90(img, 1)
#     Image.fromarray(rotate1).show()
#
#     rotate2 = np.rot90(img, 2)
#     Image.fromarray(rotate2).show()
#
#     rotate3 = np.rot90(img, 3)
#     Image.fromarray(rotate3).show()

# inspect_image()
# pixel_analysis()
# crop_image()
# grayscale()
# adjustments(50)
# inverted()
# threshold()
# resize()
# flip_image()
# rotate_image()

if __name__ == "__main__":
    print("Image Properties: 1")
    print("Pixel information: 2")
    op = int(input("Choose operation: "))

    if op == 1:
        inspect_image()
    elif op == 2:
        pixel_analysis()




