from PIL.Image import *

from random import *


def ascii(n,string):
    return ord(string[n])

def draw(i,n,string):
    (l, h) = i.size                                                 #Recupérer les dimensions de l'image pour l'afficher
    inc=0                                                           #Variable pour ne pas repeter le message dans l'image
    print("Dimension de l'image: "+str((l,h)))
    print("Longueur du message: "+str(n))
    for y in range(h):                                              #Parcour y
        for x in range(l):                                          #Parcour x
            c = Image.getpixel(i, (x, y))                           #c prend la valeur du pixel
            if(inc<n):                                              #Si le message n'a pas finit d'être ecrire
                valeur=ascii(inc,string)                            #Valeur prend la valeur de la valeur en ascii du caractere
            elif (inc==n):                                          #Si le message est finie ecrire #
                valeur=ord("#")                                     #Valeur prend la valeur en ascii de #
            else:
                valeur=randint(0,255)                               #Si le message est terminé faire du bourrage
            Image.putpixel(i, (x, y), (valeur,valeur,valeur))       #Ecrit dans le pixel
            inc+=1


#SETUP
print("Bonjour")
img=open("img.png")                                                 #Ouvre une image
message=str(input("Texte: "))                                       #Demande le message à l'utilisateur

draw(img,len(message),message)                                      #Lance la fonction draw
apercu=str(input("Voulez vous l'aperçu de l'image ?(o/n)"))         #Demande à l'utilisateur si il veut voir l'image
if(apercu=="o"):
    Image.show(img)                                                 #Affiche l'imge
img.save("img_test.png","PNG")                                      #Enregistre l'image










def run():
    value=str(input("Texte : "))
    img=open("img.png")
    draw(img)
    Image.show(img)

    for i in range(len(value)):
        print(str(value[i])+":"+str(ascii(i,value)))
