from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random
#  ImageFilter:Python中的图像滤波，主要对图像进行平滑、锐化、边界增强等滤波处理。

def randomChar():
    if random.randint(0, 1) == 0:
        return(chr(random.randint(65,90)))
    else:
        return(chr(random.randint(97,122)))
# 随机生成大小写字母

def randomBlackgroundColor():
    return(random.randint(64,255),random.randint(64,255), random.randint(64,255))
# 随机生成背景色对应的ASCII码
def randomWordColor():
    return(random.randint(32,127), random.randint(32,127), random.randint(32,127))
# 随机生成字体颜色
def createImage():
    im = Image.new("RGB", (300,80),(255,255,255))
    font = ImageFont.truetype("arial.ttf",60)
    draw = ImageDraw.Draw(im)
    for x in range(300):
        for y in range(80):
            draw.point((x, y), randomBlackgroundColor())

        words = ""
    for i in range(4):
        word = randomChar()
        draw.text((50 * i + random.randint(10,40),random.randint(0,20)),word,font = font, fill=randomWordColor())
        words += word

    img = im.filter(ImageFilter.BLUR)
    im.save("result_2.png")
    print(words)

if __name__ == "__main__":
    createImage()
