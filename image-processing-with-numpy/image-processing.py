from operations import *



#

#

#

#

#

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
    print("Show Image Properties: 1")
    print("Show Pixel information: 2")
    print("Crop Image: 3")
    print("Add Filters: 4")
    op = int(input("Choose operation: "))

    if op == 1:
        inspect_image()
    elif op == 2:
        pixel_analysis()
    elif op == 3:
        crop_image()
    elif op == 4:
        filters()




