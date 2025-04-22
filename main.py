import random
import pygame 

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('Jetpack Joyride Remake in Python!')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)
bg_color = (128, 128, 128)
lines = [0, WIDTH/4, 2*WIDTH/4, 3*WIDTH/4]
game_speed = 2
pause = False

def draw_screen(line_list):
    surface.fill('black')
    pygame.draw.rect(surface, (bg_color[0], bg_color[1], bg_color[2], 50), [0, 0, WIDTH, HEIGHT])
    screen.blit(surface, (0, 0))
    top = pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 50])
    bottom = pygame.draw.rect(screen, 'gray', [0, HEIGHT - 50, WIDTH, 50])
    for i in range(len(line_list)):
        pygame.draw.line(screen, 'black', (line_list[i],0), (line_list[i], 50),3)
        pygame.draw.line(screen, 'black', (line_list[i], HEIGHT - 50), (line_list[i], HEIGHT),3)
        if not pause:
            line_list[i] -= game_speed
            if line_list[i] < -0:
                line_list[i] = WIDTH
    return line_list, top, bot



run = True
while run:
    timer.tick(fps)
    lines, top_plat, bot_plat = draw_screen(lines)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()        