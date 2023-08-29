from PIL import Image
import os

path = os.getcwd()

for photo in os.listdir("images"):
    im = Image.open("{}\\images\\{}".format(path,photo))
    im.rotate(270).show()
