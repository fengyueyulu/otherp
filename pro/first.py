from  PIL import Image,ImageColor,ImageDraw,ImageFont

def add_num(image,text):
    font=ImageFont.truetype("arial.ttf",50)
    fontcolor=ImageColor.colormap.get("red")
    draw=ImageDraw.Draw(image)
    width, height = image.size
    draw.text((width - 50, 30), text, font=font, fill=fontcolor)
    image.show()

if __name__=='__main__':
    image=Image.open("../image/640-a5f3b.jpg")
    text='4'
    add_num(image,text)