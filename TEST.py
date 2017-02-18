import pygame

pygame.init()
Canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption("TEST")
clock = pygame.time.Clock()
closed = False

start_pos = (0,0)
while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True

    if pygame.mouse.get_pressed() == (1,0,0):
        end_pos = pygame.mouse.get_pos()
        pygame.draw.line(Canvas, (255,255,255), start_pos, end_pos,5)
        start_pos = end_pos
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
