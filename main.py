from pygame import *
from ball import*
init()

WINDOW_SIZE = 1000, 600   
FPS = 60    

screen = display.set_mode(WINDOW_SIZE) 
display.set_caption("Arkanoid")
clk = time.Clock()

running = True 
lose = False 
b=Ball(50,50,20,(255,0,0),4,4)  

player = Rect(0,0,100,100) 
player.center = (600,400) 



while running:
    for e in event.get():      
        if e.type == QUIT:          
            running = False 
    screen.fill((130,145,180))
    b.draw(screen)
    b.move()         
          

    display.update()    
    clk.tick(FPS)