from pygame import Rect, draw, K_a, K_d

class Platform:
    def __init__(self,x,y,w,h,color):
        self.x = x
        self.y = y
        self.w = w
        self.h= h
        self.color=color
        self.rect = Rect(self.x,self.y,self.w,self.h)

    def move(self):
        keys= key.get_pressed()
        if keys[K_a]:self.rect.x -= 5
        if keys[K_d]:self.rect.x += 5

    def draw(self,screen):
        draw.rect(screen,self.color,self.rect,border_radius=8)
        draw.rect(screen,(0,0,0), self.rect,2, border_radius = 8)