from pygame import *

init()
back= (200,255,255)
win_width=700
win_height=500
GREEN = (0,255,0)
window = display.set_mode((win_width,win_height))
window.fill(back)
display.set_caption('Моя первая игра')
picture = transform.scale(image.load('background.jpg'), (700,500))

class Card(sprite.Sprite):
    def __init__(self, width, height, x,y,color):
        super().__init__()
        self.rect = Rect(x,y,width, height)
        self.fill_color = color
    
    def draw(self):
        draw.rect(window,self.fill_color,self.rect)

greenCard=Card(100,100,100,250,GREEN)

run = True
while run:
    window.blit(picture, (0,0))
    greenCard.draw()
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run= False #break
    display.update()

