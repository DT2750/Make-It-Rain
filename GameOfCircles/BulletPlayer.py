from Sprite import Sprite
class BulletPlayer(Sprite):
    
    diameter = 20
    c = color(127, 238, 130)
        
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
