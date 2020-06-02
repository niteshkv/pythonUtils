from PIL import Image
import random

newImage = []
width=200
height=200
for i in range(0,width,1):
    for j in range(0,height,1):
        newImage.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
newIm = Image.new('RGB', (width, height))
newIm.putdata(newImage)
newIm.show()
