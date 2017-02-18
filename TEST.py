import pygame, sys

pygame.init()
pygame.font.init()
Canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption("DRAWING PAD")
clock = pygame.time.Clock()
closed = False
size = 5

#pygame.mouse.set_cursor(*pygame.cursors.arrow)

erase = False
drawing = False

start_pos = None
while not closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True

    sys_font = pygame.font.SysFont("None",20)

    e_button = pygame.draw.rect(Canvas, (255,255,255), (10,10,49,20), 0)

    text = sys_font.render("ERASE",0,(0,0,0))
    Canvas.blit(text,(10,10))
    
    if not drawing and e_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() == (1,0,0):
        erase = not erase
        print(erase)
        
    if not erase:
        col = (255,255,255)
        size = 5
    else:
        col = (0,0,0)
        size = 50
        
    if pygame.mouse.get_pressed() == (1,0,0):
        drawing = True
        end_pos = pygame.mouse.get_pos()
        if start_pos:
            pygame.draw.line(Canvas, col, start_pos, end_pos,size)
        else:
            pygame.draw.line(Canvas, col, end_pos, end_pos,size)
        start_pos = end_pos

            
    if pygame.mouse.get_pressed() == (0,0,0):
        drawing = False
        start_pos = None
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()
quit()
