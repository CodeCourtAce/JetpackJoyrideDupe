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
lines = [0, WIDTH / 4, 2 * WIDTH / 4, 3 * WIDTH / 4]
game_speed = 12
pause = False
init_y = HEIGHT - 130
player_y = init_y
booster = True



# all the code to move lines across screen and draw bg images 
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
    return line_list, top, bottom


# draw player including animation
def draw_player():
    play = pygame.rect.Rect((120, player_y + 10), (25, 60))
    pygame.draw.rect(screen, 'blue', play, 5)
    if player_y < init_y or pause:
        if booster: # jetpack flames
            pygame.draw.ellipse(screen, 'red', [100, player_y + 50, 20, 30])
            pygame.draw.ellipse(screen, 'orange', [105, player_y + 50, 10, 30])
            pygame.draw.ellipse(screen, 'yellow', [110, player_y + 50, 5, 30])
    # jetpack, body and head
    pygame.draw.rect(screen, 'white', [100, player_y + 20, 20, 30], 0, 5)
    pygame.draw.ellipse(screen, 'orange', [120, player_y + 20, 20, 50])
    pygame.draw.circle(screen, 'orange', (135, player_y + 15), 10)
    pygame.draw.circle(screen, 'black', (138, player_y + 12), 3)
    return play


run = True
while run:
    timer.tick(fps)
    lines, top_plat, bot_plat = draw_screen(lines)
    player = draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()        