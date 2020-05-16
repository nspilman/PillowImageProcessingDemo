from PIL import Image
import numpy as np

imagefiles = ['tulip.jpg','space_needle.jpg','the_sound.jpg','skyline.jpg','rainbow.jpg']

### load image
images = [Image.open(f"./sample_images/{filename}") for filename in imagefiles]

### resize image
def resize(image,smallest_side):
    current_size = image.size
    x,y = current_size
    if x > y:
        ratio = smallest_side / y
    else:
        ratio = smallest_side / x
    return image.resize([int(side * ratio) for side in current_size])


box = (0, 0, 700, 700)
cropped_images = [resize(image,700).crop(box) for image in images]
### convert image to np Array

image_array = np.array(cropped_images[0])
first_row_of_pixels = image_array[0]
first_pixel = first_row_of_pixels[0]
red,green,blue = first_pixel

def nparray_to_image(array):
    return Image.fromarray(np.uint8(array))

nparray_to_image(image_array).show()

###generating modified np arrays
def modified_image_array(array, modification):
    output = []
    for row in array:
        new_row = []
        for pixel in row:
            new_row.append(modification(pixel))
        output.append(new_row)
    return output

def redify(pixel):
    red,green,blue = pixel
    new_red = red + 40
    if new_red > 255:
        new_red = 255
    return [new_red,green,blue]

def greenify(pixel):
    red,green,blue = pixel
    new_green = green + 40
    if new_green > 255:
        new_green = 255
    return [red,new_green,blue]

def blueify(pixel):
    red,green,blue = pixel
    new_red = red + 60
    if(new_red > 255):
        new_red = 255
    return [new_red,green,blue]

def turn_white_things_yellow(pixel):
    if sum(color for color in pixel) > 500:
        return [255,255,0]
    else:
        return pixel

new_image_array = modified_image_array(np.array(cropped_images[0]),turn_white_things_yellow)
nparray_to_image(new_image_array).show()
    
### perform logic based off of pixel values
image_arrays = [np.array(image) for image in cropped_images]
new_image_array = []
image_one_array = image_arrays[1]
image_two_array = image_arrays[2]
for row in range(len(image_one_array)):
    new_row = []
    for col in range(len(image_one_array[0])):
        pixel = image_one_array[row][col]
        if(sum(color for color in pixel)>450):
            new_row.append(image_two_array[row][col])
        else:
            new_row.append(pixel)
    new_image_array.append(new_row)

new_image = nparray_to_image(new_image_array)

new_image.show()

### Save images to file
new_image.save(f"./output/new_image.jpg")

        



