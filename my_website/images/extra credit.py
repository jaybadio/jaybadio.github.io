import os.path
import matplotlib.pyplot as plt
import numpy as np
import PIL
import PIL.ImageDraw

def openfile(filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(directory, filename)
    return PIL.Image.open(filename)

def cropimg(dansmall):
    return dansmall.crop((45,229,451,749))

    
  
def ovalmask(image):
    width = image.size[0]
    length = image.size[1]
    my_mask = PIL.Image.new('RGBA', (width, length), (0, 0, 0, 0))
    drawing_layer = PIL.ImageDraw.Draw(my_mask)
    drawing_layer.ellipse((0, 0, width, length), fill=(120, 120, 0, 255))
    result = PIL.Image.new('RGBA', (width, length))
    result.paste(image, (0, 0), mask=my_mask)
    return result

    img2 = np.array(image)
    height = len(img2)
    width = len(img2[0])
    for row in range(height):
        for column in range (width):
            pxl = sum(img2[row][column][0:3])/3
            img2[row][column] = [pxl, pxl, pxl, img2[row][column][3]]
    image = PIL.Image.fromarray(img2)
    return image
          
dan = (ovalmask(cropimg(openfile("jay.png"))))

rush = openfile("centrowitz.jpg")
dansmall = dan.resize((180, 180)) #resizes nick


rush.paste(dansmall, (1012, 107), mask=dansmall)


image = openfile("jay.png")

fig, ax = plt.subplots(1, 2)

#ax[0].imshow(image, interpolation='none')
ax[0].imshow(dansmall, interpolation='none')
ax[1].imshow(rush, interpolation='none')
dansmall.save("CSP_dan.bmp")
fig.show()