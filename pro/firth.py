import glob
from PIL import Image
glob=glob.glob(r"../image/*.jpg")
for i in glob:
    n=2
    image=Image.open(i)
    image.thumbnail((1136, 640))
    path="../image/%d.jpg"%(n)
    image.save(path)
    print(image.format, image.size, image.mode)
    n+=1
