from Sprite import Sprite

class Raindrop(Sprite):
    
    speed = 8
    diameter = 25
    c = color(92, 194, 232)
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.y = 0
