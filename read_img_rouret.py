from PIL.Image import *
from turtle import *
from random import *


def ascii(number):
    return chr(number)


def decrypt(i):
    (l, h) = i.size
    end=False
    print("Dimension de l'image: "+str((l,h)))
    for y in range(h):
        for x in range(l):
            c = Image.getpixel(i, (x, y))
            if (end==False):
                if(str(ascii(c[0]))!='#'):
                    print(str(ascii(c[0])),end='')
                else:
                    end=True








img=open("img_test.png")
decrypt(img)
print("End")











