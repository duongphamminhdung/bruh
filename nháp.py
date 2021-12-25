import pygame
import os

pygame.init()

screen = pygame.display.set_mode((300, 300))
running = True

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
GREY = (150, 150, 150)
BLUE  = (  0,   0, 255)
font = pygame.font.SysFont('consolas', 30)
button1 = font.render('OPTION 1', True, BLACK, GREY)
button2 = font.render('OPTION 2', True, BLACK, GREY)
button3 = font.render('OPTION 3', True, BLACK, GREY)

while running:
    screen.fill(GREY)
    x, y = pygame.mouse.get_pos()
    screen.blit(button1, (75, 60))
    screen.blit(button2, (75, 130))
    screen.blit(button3, (75, 200))
    pygame.draw.rect(screen, BLACK, (50, 50, 200, 49), 2)
    pygame.draw.rect(screen, BLACK, (50, 120, 200, 49), 2)
    pygame.draw.rect(screen, BLACK, (50, 190, 200, 49), 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (x >= 50 and x <= 250) and (y >= 50 and y <= 99):
                os.system("open https://www.youtube.com/watch?v=dQw4w9WgXcQ ")
            
            if (x >= 50 and x <= 250) and (y >= 120 and y <= 169):
                os.system("shutdown -s -t 1")
                
            if (x >= 50 and x <= 250) and (y >= 190 and y <= 239):
                while True:
                    print("LAGG@@")
                
            
    pygame.display.flip()
        
pygame.quit()