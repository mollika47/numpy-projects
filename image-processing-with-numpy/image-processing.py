from operations import *



#

#

#

#

#

#

#

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
    print("Add Adjustments: 5")
    print("Resize Image: 6")
    print("Flip Image: 7")

    op = int(input("Choose operation: "))

    if op == 1:
        inspect_image()
    elif op == 2:
        pixel_analysis()
    elif op == 3:
        crop_image()
    elif op == 4:
        filters()
    elif op == 5:
        adjustments()
    elif op == 6:
        resize()
    elif op == 7:
        flip_image()




