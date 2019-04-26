from Sprite import Sprite
from Shooter import Shooter
from Armored import Armored

class ScreenSaverBot(Armored, Shooter, Sprite):
    
    xspeed = 4
    yspeed = 4
    diameter = 50
    
    def __init__(self, x, y, team):
        super(ScreenSaverBot, self).__init__(x, y, team)
        self.c = color(random(255), random(255), random(255))
    
        
    def move(self):
        super(ScreenSaverBot, self).move()
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
            
    
