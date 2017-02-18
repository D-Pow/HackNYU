import pygame
pygame.init()
Canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption("TEST")
clock = pygame.time.Clock()
closed = False

while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
    print(event)
       
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
