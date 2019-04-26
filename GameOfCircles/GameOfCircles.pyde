import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Armored import Armored
import SpriteManager
from PlayerShooter import PlayerShooter

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(800, 600)
    
    player = Player(width/ 2, height - 100, 1)
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(ScreenSaverBot(random(width), random(height), 2))
    SpriteManager.spawn(ScreenSaverBot(random(width), random(height), 2))
    SpriteManager.spawn(ScreenSaverBot(random(width), random(height), 2))
                           
def draw():
    background(255)
    SpriteManager.animate()    
    
def keyPressed():
    global player
    SpriteManager.getPlayer().keyDown()

def keyReleased():
    SpriteManager.getPlayer().keyUp()
    
def mousePressed():
    SpriteManager.getPlayer().mouseDown()
