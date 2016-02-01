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
        self.Shield = !self.Shield

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

        
def display(Pics):
    screen.blit(background_image, background_position)
    screen.blit(Pics.get_img(), Pics.get_rect())

    pygame.display.flip()
    screen.blit
	  pygame.time.wait(15)

#TODO Display elements
