
'''
Import the following: sys, pygame, random
from ship import Ship
from asteroid import Asteroid
from pygame.locals import *

Call pygame.init()
create a variable called "screen_info" set it equal to pygame.display.Info()

'''




import sys, pygame, random
from ship import Ship
from asteroid import Asteroid
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)

# read and store game data
#df = pd.read_csv('game_info.csv')




# Setup Game Variables
asteroids = []


Asteroids = pygame.sprite.Group()
NumLevels = 3
Level = 0
#LevelData = df.iloc[Level]
AsteroidCount = 3
Player = Ship((20, 200))


'''
Define an "init method":
globals - AsteroidCount,Asteroids
Call player.reset to 20,200
Call Asteroids.empty()
Set Asteroid count to 3
Create a for loop that runs "AsteroidCount" times
'''







def init():
    global AsteroidCount, Asteroids#, LevelData
    #LevelData = df.iloc[Level]
    Player.reset((20, 200))
    Asteroids.empty()
    AsteroidCount = 3
    for i in range(AsteroidCount):
        Asteroids.add(Asteroid((random.randint(50, width - 50), random.randint(50, height - 50)), random.randint(15, 60)))



def win():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You Escaped!", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()





def main():
  global Level
  while Level <= NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
              print("move right")
            if event.key == pygame.K_LEFT:
              print("move right")
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
              print("move right")












def main():
    global Level
    init()
    while Level <= NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Player.speed[0] = 10
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = -10
                if event.key == pygame.K_UP:
                    Player.speed[1] = -10
                if event.key == pygame.K_DOWN:
                    Player.speed[1] = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    Player.speed[0] = 0
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = 0
                if event.key == pygame.K_UP:
                    Player.speed[1] = 0
                if event.key == pygame.K_DOWN:
                    Player.speed[1] = 0

        screen.fill(color)
        Player.update()
        Asteroids.update()
        gets_hit = pygame.sprite.spritecollide(Player, Asteroids, False)
        Asteroids.draw(screen)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()

        if Player.checkReset(width):
            if Level == NumLevels:
                break
            else:
                Level += 1
                init()
        elif gets_hit:
            Player.reset((20, 200))

    win()


if __name__ == '__main__':
    main()
