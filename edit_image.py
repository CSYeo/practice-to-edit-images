from PIL import Image
import os

for photo in os.listdir("images"):
    print(photo)
#    im = Image.open(photo)
#    im.rotate(90).show()
