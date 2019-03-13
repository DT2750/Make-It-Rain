from Sprite import Sprite
from Shooter import Shooter

class ScreenSaverBot(Shooter, Sprite):
    
    xspeed = 8
    yspeed = 4
    diameter = 50
    c = color(193, 99, 226)
        
    def move(self):
        super(ScreenSaverBot, self).move()
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
