import pygame

pygame.init()
Canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption("DRAWING PAD")
clock = pygame.time.Clock()
closed = False

start_pos = None
while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
    if pygame.mouse.get_pressed() == (1,0,0):
        end_pos = pygame.mouse.get_pos()
        if start_pos:
            pygame.draw.line(Canvas, (255,255,255), start_pos, end_pos,5)
        else:
            pygame.draw.line(Canvas, (255,255,255), end_pos, end_pos,5)
        start_pos = end_pos
    if pygame.mouse.get_pressed() == (0,0,0):
        start_pos = None
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
        
