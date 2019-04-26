import SpriteManager

from BulletPlayer import BulletPlayer
from Sprite import Sprite

class PlayerShooter:
        
    def aim(self):
        
        distance = dist(mouseX, mouseY, self.x, self.y)
        xComponent = mouseX - self.x
        yComponent = mouseY - self.y
        
        if distance == 0:
            distance = 0.01
            
        magnitude = 10
        return PVector(xComponent / distance * magnitude, yComponent / distance * magnitude)
    
    def fire(self, vector):
        SpriteManager.spawn(BulletPlayer(self.x, self.y, vector, self.team))
    
