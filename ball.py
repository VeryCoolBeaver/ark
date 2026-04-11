from pygame import Rect, draw,other
class Ball:
    def __init__(self,x,y,r,color,vx=None,vy=None):
        self.x = x
        self.y = y
        self.r=r
        self.color = color
        self.vx = vx if vx is not None else 5
        self.vy = vy if vy is not None else 5
        self.rect=Rect(0,0,r,r)
        self.rect.center= (self.x,self.y)

    def check_collision(self,):
        return self.rect.colliderect(other.rect)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.center= (self.x,self.y)

        if self.x + self.r <0 or self.x + self.r>1000:
            self.vx *=-1
        if self.y - self.r <0 or self.y + self.r >600:
            self.vy *= -1

    def draw(self,screen):
        draw.circle(screen,self.color, (self.x,self.y),self.r)