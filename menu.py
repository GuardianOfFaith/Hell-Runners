import pygame
from pygame.locals import *
import os
import sys

# Methode permettant de charger une image
# et renvoyant l'objet surface associee 
def load_image(name):
    image = pygame.image.load(name)
    return image

# Init modules pygames
pygame.init()

# Init variable globales
page_active = "menu"

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

# Lance la musique
#pygame.mixer.music.load('music.mp3')
#pygame.mixer.music.play()

# Game loop
while 1:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		sys.exit()

        if event.type == MOUSEBUTTONUP and event.button == 1:
            if event.pos[0] >= 500 and event.pos[0] <= 600 and event.pos[1] >= 50 and event.pos[1] < 150 and page_active == "menu":
                #lancer le jeu
                print("Lancement du jeu")

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
