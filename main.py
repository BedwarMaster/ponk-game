#1 import stuff
from pygame import *
from random import *

#create window 
WIDTH, HEIGHT = 800,640
window = display.set_mode((WIDTH,HEIGHT))
clock = time.Clock()

#createclasses
class  ImageSprite(sprite.Sprite):
    def __init__(self, filename, pos, size):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image,size)
        self.rect = Rect(pos, size)
        self.initial_pos = pos
    def draw(self, surface):
        surface.blit(self.image,self.rect.topleft)
    def reset(self):
        self.rect.topleft = self.initial_pos
    

class PlayerSprite1(ImageSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= 8
        if keys[K_s]:
            self.rect.y += 8   

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class PlayerSprite2(ImageSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= 8
        if keys[K_DOWN]:
            self.rect.y += 8   

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class BallSprite(ImageSprite):
    def __init__(self, filename, pos, size, speed):
        super().__init__(filename, pos, size)
        self.speed = Vector2(speed)
    def update(self):
        self.rect.topleft += self.speed
    def vertical_bounce(self):
        self.speed.y *= -1
    def horizontal_bounce(self):
        self.speed.x *= -1
    


#create player and bg
#bg = ImageSprite(filename='stadium.avif', pos=(0,0), size=(WIDTH,HEIGHT))
p1 = PlayerSprite1(filename='me.jpg', pos=(0,200), size=(100,100))
p2 = PlayerSprite2(filename='ro.jpg', pos=(700,200), size=(100,100))
ball = BallSprite(filename='ball.jpg', pos=(WIDTH/2,HEIGHT/2), size=(70,70), speed=(0.1 ,100))

while not event.peek(QUIT):
    #bg.draw(window)
    window.fill((165, 245, 6))
    p1.update()
    p1.draw(window)
    p2.update()
    p2.draw(window)
    ball.update()
    ball.draw(window)

    if ball.rect.top < 0 or ball.rect.bottom > HEIGHT:
        ball.vertical_bounce()
    

    





    display.update()
    clock.tick(60)