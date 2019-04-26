import SpriteManager
from BulletPlayer import BulletPlayer
from Sprite import Sprite
from PlayerShooter import PlayerShooter

class Player(Sprite, PlayerShooter):
    
    # instance variables
    left = False
    right = False
    up = False
    down = False
    speed = 7.5
    diameter = 50  
    c = color(28, 33, 160)
    
    def handleCollision(self):
        pass
    
    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)
        
    def mouseDown(self):
        self.fire(self.aim())
            
    def keyDown(self):
        if key == 's' or key == 'S':
            SpriteManager.spawn(BulletPlayer(self.x, self.y, PVector(0, 10), self.team))
        if key == ' ' or key == 'w':
            SpriteManager.spawn(BulletPlayer(self.x, self.y, PVector(0, -10), self.team))
            
        if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
            
