import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    size(650, 650)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height - 100, playerTeam)
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(ScreenSaverBot(200, 100, 4))
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    
    SpriteManager.spawn(Enemy(0, 0, enemyTeam))
    SpriteManager.spawn(Enemy(100, 100, enemyTeam))
    SpriteManager.spawn(Raindrop(50, 50, enemyTeam))
    SpriteManager.spawn(Raindrop(100, 100, enemyTeam))
    SpriteManager.spawn(Raindrop(150, 150, enemyTeam))
    SpriteManager.spawn(Raindrop(200, 200, enemyTeam))
    SpriteManager.spawn(Raindrop(250, 250, enemyTeam))
    SpriteManager.spawn(Raindrop(300, 300, enemyTeam))
    SpriteManager.spawn(Raindrop(450, 450, enemyTeam))
    SpriteManager.spawn(Raindrop(500, 500, enemyTeam))
    SpriteManager.spawn(Raindrop(550, 550, enemyTeam))
    SpriteManager.spawn(Raindrop(600, 600, enemyTeam))
    SpriteManager.spawn(JiggleBot(width/2, height/2, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(0, 0, enemyTeam))
                           
def draw():
    background(255)
    SpriteManager.animate()    
    
def keyPressed():
    global player
    SpriteManager.getPlayer().keyDown()    
        
def keyReleased():
    global player
    SpriteManager.getPlayer().keyUp()
