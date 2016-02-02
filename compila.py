import sys
import pygame
from pygame.locals import *
import os
import random

#fonction et classes
#objets
def load_image(name):
    image = pygame.image.load(name)
    return image

class Object():
    # constructeur
    def __init__(self, pos_x, etage, image):

        #initialisation et affectation d'attribut
        self.image = load_image(image)
        self.rect = pygame.Rect(pos_x, etage, 25, 25)

    def get_rect(self):
        return self.rect

    def get_img(self):
        return self.image


class Personnage(Object):
    def __init__(self, pos_x, etage, image, hp, Shield):
        Object.__init__(self, pos_x, etage, image)

    def get_hp(self):
        return self.hp

    def set_hp(self, val):
        self.hp = val

    def get_shield(self):
        return self.Shield

    #/!\ conditions a controler
    def update_shield(self):
        self.Shield = not self.Shield

    def deplacement(self):
        self.pos_x = self.pos_x
        #TODO

    #TODO interraction objet
    def alive(self):
        if Personnage.get_hp==0:
            sys.exit()
            print "GAME OVER"

class Pics(Object):
    def __init__(self, pos_x, etage):
        Object.__init__(self, pos_x, etage, "assets/Pics.png")
    def damage(Personnage):
        if Personnage.get_shield!=True :
            Personnage.update_shield
        else :
            Personnage.set_hp(get_hp-1)


class Heart(Object):
    def __init__(self, pos_x, etage):
        Objet.__init__(self, pos_x, etage, "assets/Heart.png")

    def heal(Personnage):
        if Personnage.get_hp<3:
            Personnage.set_hp(Personnage.get_hp+1)
            self.pos_x =6666
            self.etage =6666


class Block(Object):
    def __init__(self, pos_x, etage):
        objet.__init__(self, pos_x, etage, "assets/Block.png")

class Passerelle(Object):
    def __init__(self, pos_x, etage):
        objet.__init__(self, pos_x, etage, "assets/Passerelle.png")

class End(Object):
    def __init__(self, pos_x, etage):
        Object.__init__(self, pos_x, etage, "assets/End.png")
    #TODO interraction

class Shield(Object):
    def __init__(self, pos_x, etage):
        Object.__init__(self, pos_x, etage, "assets/Shield.png")

    def defense(Personnage):
        if Personnage.get_shield==False:
            Personnage.update_shield
            self.pos_x =6666
            self.etage =6666

def display(Pics):
    screen.blit(background_image, background_position)
    screen.blit(Pics.get_img(), Pics.get_rect())

    pygame.display.flip()
    screen.blit
	  #pygame.time.wait(15)

#TODO Display elements

#fin objets

#TODO genDrop & gen
def genDrop():
    #generateur d'objet
    rand=random.randint(0,9)
    #if rand == 3 :
        #Heart
    #elif rand == 7 :
        #Shield
    #elif rand == 1 and rand == 5 and rand == 9 :
        #Pics


def gen():
    #generateur de map
    map = array([[0,1,2,3,4,5,6,7,8,9,10,11],[0,1,2]])
    #creation map sur i etage
    j=0
    while j < 3:
        k=0
        while k<12:
            rand = random.randint(0,4)
            if rand == 1 and rand == 3 :
                #creation Block
                map[k][j]=Block(k,j)
                genDrop(map[k][j])
            elif rand == 2 and rand == 4 :
                #creation Passerelle
                map[k][j]=Passerelle(k,j)
                genDrop(map[k][j])
            k=k+1
        j=j+1
    map[0][0]=Block(0,0)
    map[11][0]=Block(11,0)


#system du jeu
def game_loop():
    #creation map
    gen()
    #creation personnages
    joueur= Personnage(0,0,"",3,False)
    IA = Personnage(11,0,"",3,False)

    #boucle de jeu
    while 1:

        joueur.alive(self)
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        	    sys.exit()


        #Deplacement

        #Calculs


        #Affichage

def menu() :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONUP and event.button == 1:
            if event.pos[0] >= 500 and event.pos[0] <= 600 and event.pos[1] >= 50 and event.pos[1] < 150 and page_active == "menu":
                #lancer le jeu
                game_loop()

            if event.pos[0] >= 500 and event.pos[0] <= 600 and event.pos[1] >= 150 and event.pos[1] < 250 and page_active == "menu":
                #chargement des instructions
                print("Chargement de la page des instructions")
                #pygame.display.update(screen.fill(0))
                page_active = "instruction"
                pygame.display.update(screen.blit(background_image, background_position))


            if event.pos[0] >= 500 and event.pos[0] <= 600 and event.pos[1] >= 250 and event.pos[1] <= 350 and page_active == "menu":
                sys.exit()


    # Ajoute notre images a la file des affichages prevus
    screen.blit(background_image, background_position)
    if page_active == "menu":
        screen.blit(menu_image, menu_position)
        screen.blit(jouer_image, jouer_position)
        screen.blit(instruction_image, instruction_position)
        screen.blit(quitter_image, quitter_position)
    elif page_active == "instruction":
        screen.blit(background_instruction_image,background_instruction_position)
        screen.blit(touche_deplacement_image,touche_deplacement_position)
        screen.blit(touche_objet_image,touche_objet_position)
        screen.blit(touche_menu_image,touche_menu_position)


    # Affiche toute la liste FIFO (ici que notre image de fond)
    pygame.display.flip()
    screen.blit


###########################################################

# initialise les modules pygame
pygame.init()

# Init variable globales
page_active = "menu"

#initialisation Musique
#TODO

# Charge l'image de fond
background_image = load_image("background.jpg")
background_position = [0, 0]

##############
#####MENU#####
##############

# Charge l'image de menu
menu_image = load_image("menu.jpg")
menu_position = [500, 50]

#Charge le boutton jouer
jouer_image = load_image("jouer.png")
jouer_position = [500, 50]

#Charge le boutton instruction
instruction_image = load_image("instruction.png")
instruction_position = [500, 150]

#Charge le boutton quitter
quitter_image = load_image("quitter.png")
quitter_position = [500, 250]

######################
#####INSTRUCTIONS#####
######################

#Charge le fond de la page instructions
background_instruction_image = load_image("background_instruction.png")
background_instruction_position = [20, 20]

# Charge les touches de deplacement
touche_deplacement_image = load_image("touches.png")
touche_deplacement_position = [50, 50]

#Charge les touches d'objets
touche_objet_image = load_image("touches-a_ctrl.png")
touche_objet_position = [50, 130]

#Charge les touches du menu
touche_menu_image = load_image("touches-e_0.png")
touche_menu_position = [50, 250]

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

while 1:
    menu()
