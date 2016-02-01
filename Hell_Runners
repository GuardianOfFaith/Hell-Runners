import sys
import pygame
import os

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

class Pics(Object):
    def __init__(self, pos_x, etage):
        Object.__init__(self, pos_x, etage, "assets/Pics.png")

    # definition des effets
    
def display(Pics):
    screen.blit(background_image, background_position)
    screen.blit(Pics.get_img(), Pics.get_rect())

    pygame.display.flip()
    screen.blit
	  pygame.time.wait(15)
	  
#fin objets


#System de jeu

def game_loop():
    #création map
    #création personnages

    #boucle de jeu
    while 1:
        for event in pygame.event.get():
        	if event.type == pygame.QUIT:
        	    sys.exit()

        #Déplacement

        #Calculs

        
        #Affichage

###########################################################

# initialise les modules pygame
pygame.init()

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#initialisation Musique

#chargement Acceuil

#lancement boucle de jeu
game_loop();

#Affichage Instructions

#Fermer le jeu
