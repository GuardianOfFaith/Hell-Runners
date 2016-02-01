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

    #TODO interraction

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
        #TODO deplacement

    #TODO interraction objet

class Heart(Object):
    def __init__(self, pos_x, etage):
        objet.__init__(self, pos_x, etage, "assets/Heart.png")
    #TODO interraction

class Block(Object):
    def __init__(self, pos_x, etage):
        objet.__init__(self, pos_x, etage, "assets/Block.png")
    #TODO interraction

class Passerelle(Object):
    def __init__(self, pos_x, etage):
        objet.__init__(self, pos_x, etage, "assets/Passerelle.png")
    #TODO interraction

class End(Object):
    def __init__(self, pos_x, etage):
        Object.__init__(self, pos_x, etage, "assets/End.png")
    #TODO interraction
        
def display(Pics):
    screen.blit(background_image, background_position)
    screen.blit(Pics.get_img(), Pics.get_rect())

    pygame.display.flip()
    screen.blit
	  pygame.time.wait(15)

#TODO Display elements
