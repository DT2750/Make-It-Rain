import SpriteManager
from Sprite import Sprite
from Shooter import Shooter

class Armored(Shooter, Sprite):
    armor = 10
    
    def display(self):
        stroke(100)
        strokeWeight(self.armor)
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
        
    def handleCollision(self):
        self.armor -= 1
        if self.armor < 1:
            SpriteManager.destroy(self)
