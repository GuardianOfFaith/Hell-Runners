import sys
import pygame 
import os
import time
from pygame.locals import *

# Methode permettant de charger une image
# et renvoie l'objet surface associee 
def load_image(name):
    image = pygame.image.load(name)
    return image

# Init modules pygames
pygame.init()

#********************** CLASSES **********************
class Object():
    # constructeur
    def __init__(self,pos_x, etage, image,degat):

        #initialisations et affectations des attributs :
        self.degat = degat
        self.image = load_image(image)
        self.rect = pygame.Rect(pos_x, etage, self.image.get_width(), self.image.get_height())

    def get_rect(self):
        return self.rect

    def get_img(self):
        return self.image

    def get_changement(self):
        return self.degat

class Personnage(Object):
    def __init__(self, pos_x, etage, image, hp, Shield):
        Object.__init__(self, pos_x, etage, image,0)
        self.hp = hp
        self.Shield = Shield

    def get_hp(self):
        return self.hp

    def set_hp(self, val):
        self.hp = val

    def get_shield(self):
        return self.Shield

    def set_changement(self,changement):
        self.hp = self.hp + changement

    def update_shield(self):
        self.Shield =  not self.Shield

    def deplacement(self):
        self.pos_x = self.pos_x
        #TODO
    def alive(self):
        if getattr(self,"hp") ==0:
            #Init boite dialogue
            font = pygame.font.Font(None, 150)
            text = font.render("WASTED", 1, (205, 51, 51))
            textpos = text.get_rect()
            textpos.centerx = screen.get_rect().centerx
            textpos.centery = screen.get_rect().centery
            #Affichage de message de fin
            background_image = load_image("Background/sLoose.png")
            screen.blit(background_image, background_position)
            
            screen.blit(text,textpos)
            pygame.display.flip()
            screen.blit
            #Laisse le temps de lire
            time.sleep(3)
            #Exit
            sys.exit()
    def posX(self):
        return pos_x
    def posEtage(self):
        return etage
      
class Shield(Object):
    def __init__(self, pos_x, etage):
        Object.__init__(self, pos_x, etage, "assets/Shield.png")

    def defense(Personnage):
        if Personnage.get_shield==False:
            Personnage.update_shield

def isPointInsideRect(x, y, rect):
  if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
    return True
  else:
    return False

def doRectsOverlap(rect1, rect2):
  #Principes de l'algorithme : https://inventwithpython.com/chapter18.html
  for a, b in [(rect1, rect2), (rect2, rect1)]:
    #1/2 X
    heroMiddle = (a.left + a.right)/2
    #Touche par le bas : return 0
    if (isPointInsideRect(a.left, a.bottom, b) or isPointInsideRect(a.right, a.bottom, b) or isPointInsideRect(heroMiddle, a.bottom, b)):
      return 0
    #Touche par le haut : return 1
    elif (isPointInsideRect(a.left, a.top, b) or isPointInsideRect(a.right, a.top, b) or isPointInsideRect(heroMiddle, a.top, b)):
      return 1
      #Si touche rien : return 2
    else:
      return 2

def collisionLateral(rect1, rect2):
  #En entree : Le joueur ou le bot et l'objet a tester :
  for a, b in [(rect1, rect2), (rect2, rect1)]:
    #Centre de l'object a ramasser :
    objMidX = (b.left + b.right)/2
    objMidY = (b.top + b.bottom)/2
    #Touche l'objet : return 1
    if(isPointInsideRect(objMidX, objMidY,a)):
      return 1
    #Ne touche pas l'oject : return 0
    else:
      return 0
#********************************************************
#*****************Chargements des images*****************
#********************************************************
    #BackGround :getattr(Hero,"Shield") == True
background_image = load_image("Background/Background.png")
background_position = [0, 0]
    #Personnages
        #Joueur :
Hero = Personnage(0,0,"animation/player/spartiatDroite.png",2,False)
hero_rect = Hero.get_rect().move(0,0)

        #IA :
    #A faire !
    #Objects
        #Pics :
pics = Object(0,0,"assets/Pics.png",-1)
pics_rect = pics.get_rect().move(300,420)
        #Block :
block = Object(0,0,"assets/Block.png",0)
block_rect = block.get_rect().move(350,250)
        #Passerelles :
passerelle = Object(0,0,"assets/Passerelle.png",0)
passerelle_rect = passerelle.get_rect().move(240,400)
        #Coeurs :
vie = load_image("assets/Heal_1.png")
black_heart = load_image("assets/BlackHeart.png")
        #Coeur / heal
heal = Object(0,0,"assets/Heal_1.png",1)
        #Shield :
shield = Object(0,0,"assets/Shield_1.png",5)
        #Murs
lWall = load_image("assets/Wall-Left.png")
rWall = load_image("assets/Wall-Right.png")

#*****************Affiche la fenetre*****************
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#*****************Lance la musique*****************
pygame.mixer.music.load('Dragonforce - Through The Fire And Flames (8 Bit).mp3')
pygame.mixer.music.play()

#Positionne Item : 
heal_rectIt = heal.get_rect().move(400,440)
shield_rectIt = shield.get_rect().move(100,440)

#Positionne le "HUD" :
vie_rect1HUD = vie.get_rect().move(15,15)
vie_rect2HUD = vie.get_rect().move(40,15)
vie_rect3HUD = vie.get_rect().move(65,15)
emptyHeart1HUD = black_heart.get_rect().move(15,15)
emptyHeart2HUD = black_heart.get_rect().move(40,14)
emptyHeart3HUD = black_heart.get_rect().move(65,14)
shield_rectHUD = shield.get_rect().move(width -35,15)


#*****************Variables*****************
    #Constantes
#Hauteur des Sauts :
h = 100
#Gravite : 
g = 15
#Vitesse remontee saut :
vs = -30
#Vitesse lateral :
sp = 10

    #Boolean :
peutsauter= True
ascension = False
var3 = True
    #Integer :
var = 1
var2 = 1
    #Clock :
#Initialisation de la fonction clock() : 
time.clock() 
#Stockage du temps :
immunity = time.clock() 

#***************************************************
#*****************  Boucle de Jeu  *****************
#***************************************************

while 1:
    #Sortie de la boucle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    #Test pour savoir si le joueur est en vie :
    Hero.alive()

    #***************** Deplacement Personnage *****************
    #Lecture de la touche pressee : 
    keys = pygame.key.get_pressed()

    #Saut :
    if (keys[pygame.K_UP] or keys[pygame.K_z]) and peutsauter and doRectsOverlap(hero_rect,pics_rect) != 1:               
        # A BOUGER !    Hero.set_changement(pics.get_changement())
            ascension = True
            peutsauter= False
            posBotHero = hero_rect.bottom 

    #Affichage de face a la fin du mouvement :
    if var3:
        hero = load_image("animation/player/f.png")
    else:
        hero = load_image("animation/player/f.png")

    # Deplacement a gauche :
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        hero_rect = hero_rect.move(-sp,0)
        if var == 1 or var == 2:
            hero = load_image("animation/player/g1.png")
            var = var +1
            var3 = True
        elif var == 3 or var ==4 :
            hero = load_image("animation/player/g2.png")
            var = var +1
            var3 = True
        elif var == 5 or var == 6:
            hero = load_image("animation/player/g3.png")
            var = 1
            var3 = True

    # Deplacement a droite :
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        hero_rect = hero_rect.move(sp,0)
        if var2 == 1 or var2 == 2:
            hero = load_image("animation/player/d1.png")
            var2 = var2 +1
            var3 = False
        elif var2 == 3 or var2 ==4 :
            hero = load_image("animation/player/d2.png")
            var2 = var2 +1
            var3 = False
        elif var2 == 5 or var2 == 6:
            hero = load_image("animation/player/d3.png")
            var2 = 1
            var3 = False

    #Teleportation de l'autre cote de l'ecran :
    if hero_rect.right > width+15:
        hero_rect = hero_rect.move(-620,0)
    if hero_rect.left < -15:  
        hero_rect = hero_rect.move(620,0)

    #Gravite (Le personnage descend tant qu'il n'est pas sur une plateforme) :
    if hero_rect.bottom < height and doRectsOverlap(hero_rect, pics_rect) != 0:
        hero_rect = hero_rect.move(0,g)

    #Joueur peut ressauter si il touche le sol ou une plateforme : 
    if hero_rect.bottom >= height:
        peutsauter = True
    if(doRectsOverlap(hero_rect,pics_rect) == 0):
        peutsauter=True

    #Saut avec vitesse : 
    if ascension and doRectsOverlap(hero_rect,pics_rect) != 1:
        if hero_rect.bottom <= posBotHero -h:
            ascension = False
        else:
            hero_rect = hero_rect.move(0,vs)
    else:
        ascension = False

    #Test des degats :
    if((doRectsOverlap(hero_rect,pics_rect) == 0) and (getattr(Hero,"hp") > 0) and (time.clock() >= immunity)):
        if(getattr(Hero,"Shield") == True):
            Hero.update_shield()
        else:
            Hero.set_changement(getattr(pics,"degat"))
            hero = load_image("animation/player/fdegat.png")
        immunity = time.clock()+0.2

    #Test de Heal + shield :
    if (collisionLateral(hero_rect,shield_rectIt)):
        if(getattr(Hero,"Shield") == False):
	  Hero.update_shield()
	  shield_rectIt=shield_rectIt.move(1000,1000)
    elif(collisionLateral(hero_rect,heal_rectIt) and getattr(Hero,"hp") < 3 ):
	  Hero.set_changement(getattr(heal,"degat"))
	  heal_rectIt=heal_rectIt.move(1000,1000)
    print getattr(Hero,"hp")

    #******************************************************************
    #***************************Affichage******************************
    #******************************************************************

    #BackGround :
    screen.blit(background_image, background_position)

    #Affichage de la vie :
    if(Personnage.get_hp(Hero) >= 1):
        screen.blit(vie, vie_rect1HUD)
        screen.blit(black_heart,emptyHeart2HUD)
        screen.blit(black_heart,emptyHeart3HUD)
        if(Personnage.get_hp(Hero) >= 2):
            screen.blit(vie, vie_rect2HUD)
            screen.blit(black_heart,emptyHeart3HUD)
            if(Personnage.get_hp(Hero) == 3):
                screen.blit(vie, vie_rect3HUD)
    else:
        screen.blit(black_heart,emptyHeart1HUD)
        screen.blit(black_heart,emptyHeart2HUD)
        screen.blit(black_heart,emptyHeart3HUD)

    #Affichage des boucliers :
    if (Personnage.get_shield(Hero) == True):
        screen.blit(shield.get_img(),shield_rectHUD)
    
    #Items :
    screen.blit(shield.get_img(),shield_rectIt)
    screen.blit(heal.get_img(),heal_rectIt)

    #Others :
    screen.blit(hero, hero_rect)
    screen.blit(block.get_img(), block_rect)
    screen.blit(pics.get_img(),pics_rect)
    screen.blit(passerelle.get_img(),passerelle_rect)

    #Affiche toute la file
    pygame.display.flip()
    screen.blit
    time.sleep(0.03)
