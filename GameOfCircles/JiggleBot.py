from Sprite import Sprite
from Shooter import Shooter

class JiggleBot(Shooter, Sprite):
    
    speed = 4
    diameter = 75
    c = color(42, 130, 50)
        
    def move(self):
        super(JiggleBot,self).move()
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
        
    def display(self):
        fill(self.c)
        stroke(0)
        strokeWeight(10)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()

        
