from pygame import Rect, draw
class Block:

    def __init__(self,x,y,w,h,color):
        self.x = x
        self.y = y
        self.w = w
        self.h= h
        self.color = color
        self.rect= Rect(x,y,w,h)

    def draw(self,screen):
        draw.rect(screen, self.color, self.rect)