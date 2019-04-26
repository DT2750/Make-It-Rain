from Sprite import Sprite
from Shooter import Shooter
from Armored import Armored

class JiggleBot(Armored, Sprite):
    
    speed = 4
    diameter = 75
    c = color(42, 130, 50)
        
    def move(self):
        super(JiggleBot,self).move()
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)

        
