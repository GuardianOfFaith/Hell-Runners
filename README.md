# Hell-Runners
Game Jam 2016 
Iut2 Grenoble
Equipe 404SkillNotFound


Presentation du jeu :


Classes :
  Object
    # __init__ (self, pos_x, etage, image) 
    # get_rect(self)
    # get_img(self)

  Personnage extends Object
    - __init__ (self, pos_x, etage, image, hp, Shield)
    - get_hp(self)
    - set_hp(self)
    - get_shield(self)
    - update_shield(self)
    - deplacement(self) #TODO
    - alive(self)

  Pics extends Object
    - __init__(self, pos_x, etage)
    - damage(Personnage)
    
  Heart extends object
    - __init__ (self, pos_x, etage)
    - heal (personnage)
    
  Block extends Object
    - __init__(self, pos_x, etage)
    
  Passerelle extends Object
    - __init__(self, pos_x, etage)
    
  End Object
    - __init__(self, pos_x, etage)
    - Victoire #TODO
  
  Shield Object
    - __init__(self, pos_x, etage)
    - defense (Personnage)
    
  
