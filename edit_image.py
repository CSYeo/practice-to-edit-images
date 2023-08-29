from PIL import Image
import os

for photo in os.listdir("images"):
    im = Image.open("{}\\images\\{}".format(os.getcwd(),photo))
    im.rotate(90).show()
